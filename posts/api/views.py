from rest_framework.generics import ListAPIView
from posts.models import Post
from .serializers import PostSerializer


class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    