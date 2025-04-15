from django.shortcuts import render

# Create your views here.
def burping(request):
    return render(request, 'burping.html')