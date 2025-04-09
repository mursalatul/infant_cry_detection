from django.shortcuts import render

# Create your views here.
def cry_detection_view(request):
    return render(request, 'cry-detection.html')