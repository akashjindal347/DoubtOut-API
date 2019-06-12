from rest_framework.generics import ListAPIView
from blog.models import Subject
from .serializers import SubjectSerializer


class PostAPIView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    