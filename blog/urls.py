
from django.urls import path,include
from .views import SubjectView

urlpatterns = [
   path('subjects/',SubjectView, name = 'subjects')
]
