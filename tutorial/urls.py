from django.urls import path
from tutorial import views

urlpatterns = [
    path('/tutorial', views.tutorial, name='tutorial'),
]