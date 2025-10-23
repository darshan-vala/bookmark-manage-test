from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookmarkViewSet, fetch_external_users, bookmark_chart_view, bookmark_chart_data

router = DefaultRouter()
router.register(r'bookmarks', BookmarkViewSet, basename='bookmark')

urlpatterns = [
    path('', include(router.urls)),
    path('external-users/', fetch_external_users, name='external-users'),
    path('chart/', bookmark_chart_view, name='chart-view'),         
    path('chart-data/', bookmark_chart_data, name='chart-data')
]
