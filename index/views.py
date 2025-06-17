from django.shortcuts import render
from result.models import TrustCounter
from index.models import FAQ
# Create your views here.

def index(request):
    # trust counter
    trust_count, created = TrustCounter.objects.get_or_create(id=1)
    
    # faq question & answers
    faq_data = FAQ.objects.all()
    print(faq_data)
    print("ok")
    return render(request, 'index.html', {'trust_count': trust_count.count_number, 'faq_data': faq_data,})

