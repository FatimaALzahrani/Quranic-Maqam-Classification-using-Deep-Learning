from flask import Flask, render_template, request, jsonify
import numpy as np
import librosa
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = tf.keras.models.load_model('model.h5')
encoder = LabelEncoder()
encoder.classes_ = np.load('classes.npy')

scaler = StandardScaler()
scaler.mean_ = np.load('scaler_mean.npy')
scaler.scale_ = np.load('scaler_scale.npy')

def extract_features(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, sr=22050)
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=26)
        return np.mean(mfccs.T, axis=0)
    except Exception as e:
        print(f"Error extracting features: {str(e)}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

maqam_translation = {
    'Ajam': 'عجم',
    'Bayat': 'بيات',
    'Hijaz': 'حجاز',
    'Kurd': 'كرد',
    'Nahawand': 'نهاوند',
    'Rast': 'رست',
    'Saba': 'صبا',
    'Seka': 'سيكا'
}

@app.route('/predict', methods=['POST'])
def predict():
    if 'audio_file' not in request.files:
        return jsonify({'error': 'No file part'}) 
    
    file = request.files['audio_file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(audio_path)  
    
    features = extract_features(audio_path)
    if features is None:
        return jsonify({'error': 'Failed to extract features'}) 
    
    features_scaled = scaler.transform(features.reshape(1, -1))
    prediction = model.predict(features_scaled)
    
    predicted_maqam = encoder.inverse_transform([np.argmax(prediction)])[0]
    confidence = np.max(prediction) * 100 
    translated_maqam = maqam_translation.get(predicted_maqam, 'غير معروف')

    return jsonify({'maqam': translated_maqam, 'confidence': round(confidence, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
