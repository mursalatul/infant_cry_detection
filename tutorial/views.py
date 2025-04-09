from django.shortcuts import render

# Create your views here.
def tutorial(request):
    return render(request, 'tutorial/tutorial.html')