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
from result.models import TrustCounter

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

def convert_to_wav(file_path):
    """Convert non-WAV files to WAV using pydub."""
    try:
        if file_path.lower().endswith('.wav'):
            return file_path
        wav_path = os.path.splitext(file_path)[0] + '.wav'
        audio = AudioSegment.from_file(file_path)
        audio.export(wav_path, format='wav')
        return wav_path
    except Exception as e:
        print(f"Error converting {file_path}: {e}")
        return None
    
def result(request):
    if request.method == 'POST' and 'audioFile' in request.FILES:
        audio_file = request.FILES['audioFile']

        # Save uploaded file temporarily
        file_path = default_storage.save('temp/' + audio_file.name, audio_file)
        full_path = os.path.join(settings.MEDIA_ROOT, file_path)
        # convert to wav (for any non wav file)
        full_path = convert_to_wav(full_path)
        if full_path is None:
            # conversion failed; fall back or bail out
            default_storage.delete(file_path)
            return render(request, 'result.html', {
                'prediction': 'Could not process audio file format.'})
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
        
        # 2. delete the converted WAV file
        try:
            os.remove(full_path)
        except OSError:
            pass
        # increase trust-counter database value
        if label[:5] != "Error":
            increment_trust_counter()
        return render(request, 'result.html', {'prediction': label})
        

    return render(request, 'result.html', {'prediction': 'No file uploaded'})

##########################
# prediction section end


def increment_trust_counter():
    # increase the number of times the test performed
    counter, created = TrustCounter.objects.get_or_create(id=1)
    counter.count_number += 1
    counter.save()
