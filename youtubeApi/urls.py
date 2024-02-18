from django.urls import path, include 
from .views import VideoList

urlpatterns = [
    path('videos/', VideoList.as_view(), name='video-list'),
]
