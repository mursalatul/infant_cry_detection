from django.shortcuts import render
from result.models import TrustCounter

# Create your views here.

def index(request):
    # trust counter
    trust_count, created = TrustCounter.objects.get_or_create(id=1)
    
    return render(request, 'index.html', {'trust_count': trust_count.count_number,})

