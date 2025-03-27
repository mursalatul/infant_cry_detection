from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
]