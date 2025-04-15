from django.urls import path
from belly_pain import views

urlpatterns = [
    path('/belly_pain', views.belly_pain, name='belly_pain'),
]