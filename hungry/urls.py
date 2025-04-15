from django.urls import path
from hungry import views

urlpatterns = [
    path('/hungry', views.hungry, name='hungry'),
]