
from django.urls import path,include
from .views import PostView,PostUpdateView,PostDeleteView,PostListView

urlpatterns = [
   path('create-post/',PostView, name = 'create-post'),
   path('create-post/<int:id>',PostUpdateView, name = 'update-post'),
   path('delete-post/<int:id>',PostDeleteView, name = 'delete-post'),
   path('posts',PostListView, name = 'posts'),



   

    

]
