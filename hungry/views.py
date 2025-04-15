from django.shortcuts import render

# Create your views here.
def hungry(request):
    return render (request, 'hungry.html')