from django.shortcuts import render

# Create your views here.
def discomfort(request):
    return render(request, 'discomfort.html')