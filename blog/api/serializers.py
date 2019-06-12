from rest_framework import serializers
from blog.models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        exclude = []
