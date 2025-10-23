from django.shortcuts import render
from rest_framework import viewsets
from .models import Bookmark
from .serializers import BookmarkSerializer
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse

class BookmarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on Bookmarks.
    """
    queryset = Bookmark.objects.all().order_by('priority')
    serializer_class = BookmarkSerializer

@api_view(['GET'])
def fetch_external_users(request):
    """
    A simple proxy API to fetch data from a third-party.
    """
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users?_limit=5')
        response.raise_for_status() # Raise an error for bad responses (4xx or 5xx)
        data = response.json()
        return Response(data)
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=503) # 503 Service Unavailable
    
def bookmark_chart_view(request):
    """
    Renders the HTML page that contains the chart.
    """
    return render(request, 'api/chart.html')

def bookmark_chart_data(request):
    """
    This is a new API endpoint that provides
    data for the chart.
    """
    bookmarks = Bookmark.objects.all()
    data = {
        "labels": [bookmark.title for bookmark in bookmarks],
        "data": [bookmark.priority for bookmark in bookmarks],
    }
    return JsonResponse(data)
