from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm
# Create your views here.

def PostView(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request,'createpost.html',{'form':form})

def PostUpdateView(request,id = None):
    obj = get_object_or_404(Post,id = id)
    form = PostForm(request.POST or None,instance = obj)
    if form.is_valid():
        form.save()
        return redirect('home')



    return render(request,'updatesubject.html',{'form':form})

def PostDeleteView(request,id=None):
    obj = get_object_or_404(Post,id = id)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')

    return render(request,'deleteview.html',{'obj':obj})

def PostListView(request):
    objects = Post.objects.all()
    context ={
        'objects': objects,
    }
    return render(request,'postlist.html',context)