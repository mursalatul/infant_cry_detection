from django.urls import path
from cry_detection import views

urlpatterns = [
    path('result/', views.result, name='result'),
]