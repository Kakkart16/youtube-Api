from django.urls import path, include 
from .views import VideoList, dashboard

urlpatterns = [
    path('videos/', VideoList.as_view(), name='video-list'),
    path('dashboard/', dashboard, name='dashboard'),
]
