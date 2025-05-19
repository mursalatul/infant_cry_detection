from django.urls import path
from discomfort import views

urlpatterns = [
    path('discomfort', views.discomfort, name='discomfort'),
]