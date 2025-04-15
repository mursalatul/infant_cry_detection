from django.shortcuts import render

# Create your views here.
def belly_pain(request):
    return render(request, 'belly_pain.html')