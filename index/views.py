from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
import numpy as np
import librosa
import joblib
from django.conf import settings
from pydub import AudioSegment
import pickle
from django.core.files.storage import default_storage

# Create your views here.

def index(request):
    # template = loader.get_template('D:\defence\\apps\infant_cry_detection\index\\templates\index.html')
    # return HttpResponse(template.render())
    return render(request, 'index.html')

# prediction section start
##########################

# Define class labels (same order as training)
CLASS_LABELS = ['belly_pain', 'burping', 'discomfort', 'hungry', 'tired']

# Load model once (optional for performance)
MODEL_PATH = os.path.join(settings.BASE_DIR, 'infant_cry_detection_classifier_model.pkl')
with open(MODEL_PATH, 'rb') as f:
    model, scaler = pickle.load(f)

def extract_features(audio, sr):
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    delta = librosa.feature.delta(mfccs)
    delta2 = librosa.feature.delta(mfccs, order=2)
    features = np.hstack([
        np.mean(mfccs.T, axis=0),
        np.std(mfccs.T, axis=0),
        np.max(mfccs.T, axis=0),
        np.mean(delta.T, axis=0),
        np.mean(delta2.T, axis=0)
    ])
    return features

def result(request):
    if request.method == 'POST' and 'audioFile' in request.FILES:
        audio_file = request.FILES['audioFile']

        # Save uploaded file temporarily
        file_path = default_storage.save('temp/' + audio_file.name, audio_file)
        full_path = os.path.join(settings.MEDIA_ROOT, file_path)

        try:
            # Load and extract features
            audio, sr = librosa.load(full_path, res_type='kaiser_fast')
            features = extract_features(audio, sr)
            if scaler:
                features = scaler.transform([features])
            else:
                features = [features]

            # Predict
            prediction = model.predict(features)[0]
            label = CLASS_LABELS[prediction]

        except Exception as e:
            label = f"Error during prediction: {e}"

        # Optionally delete the temp file
        default_storage.delete(file_path)

        return render(request, 'result.html', {'prediction': label})

    return render(request, 'result.html', {'prediction': 'No file uploaded'})

##########################
# prediction section end