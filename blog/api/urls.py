
from django.urls import path
from .views import PostAPIView

urlpatterns = [
    path('api/posts',PostAPIView.as_view(),name = 'api-post'),
]