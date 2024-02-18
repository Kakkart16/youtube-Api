from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Video
from .serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination

class VideoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
# Create your views here.
class VideoList(ListAPIView):
    queryset = Video.objects.all().order_by('-published_datetime')
    serializer_class = VideoSerializer
    pagination_class = VideoPagination 


