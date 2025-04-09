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

