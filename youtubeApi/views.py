from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
from .models import Video
from .serializers import VideoSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .tasks import fetch_youtube_videos

class VideoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class VideoList(ListAPIView):
    queryset = Video.objects.all().order_by('-published_datetime')
    serializer_class = VideoSerializer
    pagination_class = VideoPagination
    

def dashboard(request):
    search_query = request.GET.get('search', '')
    videos = Video.objects.all().order_by('-published_datetime')

    if search_query:
        videos = videos.filter(title__icontains=search_query)

    paginator = Paginator(videos, 10) 
    page_number = request.GET.get('page')

    try:
        videos_paginated = paginator.page(page_number)
    except PageNotAnInteger:
        videos_paginated = paginator.page(1)
    except EmptyPage:
        videos_paginated = paginator.page(paginator.num_pages)

    return render(request, 'dashboard.html', {'videos': videos_paginated, 'search_query': search_query})