from django.shortcuts import render

# Create your views here.
def tired(request):
    return render(request, 'tired.html')