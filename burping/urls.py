from django.urls import path
from burping import views

urlpatterns = [
    path('/burping', views.burping, name='burping'),
]