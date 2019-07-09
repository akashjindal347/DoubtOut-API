
from django.urls import path
from .views import PostAPIView

urlpatterns = [
    path('posts/api/',PostAPIView.as_view(),name = 'posts-api'),
]