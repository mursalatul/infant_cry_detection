from django.urls import path
from result import views

urlpatterns = [
    path('result/', views.result, name='result'),
]