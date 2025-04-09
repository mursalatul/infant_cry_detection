from django.urls import path
from cry_detection import views

urlpatterns = [
    path('cry-detection/', views.cry_detection_view, name='cry_detection_view'),
]