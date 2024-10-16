# Quranic Maqam Classification using Deep Learning

This project aims to classify Quranic maqams using deep learning techniques. A **Deep Neural Network (DNN)** model was trained on the **Maqam-478 Dataset**, consisting of various Quranic recitations, to automatically predict the maqam of a given audio file. The system utilizes **Mel-frequency cepstral coefficients (MFCC)** for audio feature extraction.

Additionally, the project includes a web interface to allow users to upload Quranic recitations and receive the predicted maqam.

## Features
- **Automatic Quranic Maqam Classification**: Upload an audio file and receive the predicted maqam.
- **Maqam Translation**: The output maqam is translated into both Arabic and English.
- **Real-time Progress Bar**: Displays a rotating progress bar while the model processes the audio file.
- **Deep Learning Model**: A pre-trained DNN model is deployed to classify the maqams.
  
## Technologies Used
- **Python** (Backend, Flask)
- **TensorFlow/Keras** (Model Training)
- **Librosa** (Audio feature extraction)
- **Google Colab** (Model Training)
- **HTML/CSS/JavaScript** (Frontend for web interface)
- **GitHub Pages** (Frontend hosting)
- **Heroku** or **PythonAnywhere** (Backend hosting)

## Maqam Classes
The following Quranic maqams are classified by the model:

- Ajam = عجم
- Bayat = بيات
- Hijaz = حجاز
- Kurd = كرد
- Nahawand = نهاوند
- Rast = رست
- Saba = صبا
- Seka = سيكا

## Setup Instructions

### Prerequisites
- Python 3.x
- Flask
- TensorFlow/Keras
- Librosa
- Numpy

### Backend Setup (Flask API)
1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/maqam-classification.git

2. Install dependencies:
   ```bash
    pip install -r requirements.txt

3. Run the Flask server:
   ```bash
    python app.py

   The Flask application will start at ```http://127.0.0.1:5000```.

## Usage
- Visit the web interface and upload an audio file in .wav format.
- Wait for the rotating progress bar to complete while the backend processes your file.
- The predicted maqam will be displayed in both English and Arabic.

## Acknowledgments
- Maqam-478 Dataset: [Link to dataset](https://figshare.com/articles/dataset/Maqam478_Qur_anic_Recitations_in_8_different_Maqams/13489359?file=26372272)
- This project was developed by Fatimah Mohammed Al-Zahrani.
