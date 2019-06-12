
from django.urls import path,include
from .views import SubjectView,SubjectDeleteView,SubjectMathsListView,SubjectScienceListView,SubjectUpdateView,HomePage

urlpatterns = [
   path('create-subject/',SubjectView, name = 'create-subject'),
   path('edit/<int:id>',SubjectUpdateView, name = 'update-subject'),
    path('maths/',SubjectMathsListView, name = 'MATHS'),
     path('science/',SubjectScienceListView, name = 'SCIENCE'),
      path('',HomePage, name = 'home'),
      path('delete/<int:id>',SubjectDeleteView, name = 'delete-subject'),

    

]
