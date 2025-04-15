from django.urls import path
from tired import views

urlpatterns = [
    path('/tired', views.tired, name='tired'),
]