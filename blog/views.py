from django.shortcuts import render,redirect
from .forms import SubjectForm
from django.shortcuts import get_object_or_404
from .models import Subject
# Create your views here.
def SubjectView(request):
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request,'createsubject.html',{'form':form})

def SubjectUpdateView(request,id = None):
    obj = get_object_or_404(Subject,id = id)
    form = SubjectForm(request.POST or None,instance = obj)
    if form.is_valid():
        form.save()
        return redirect('home')



    return render(request,'updatesubject.html',{'form':form})

def SubjectDeleteView(request,id=None):
    obj = get_object_or_404(Subject,id = id)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')

    return render(request,'deleteview.html',{'obj':obj})

def HomePage(request):
    return render(request,'home.html',{})


def SubjectMathsListView(request):
    objects = Subject.objects.filter(subject__iexact= "MATHS")

    return render(request,'onesubjectlistview.html',{'objects':objects})



def SubjectScienceListView(request):
    objects = Subject.objects.filter(subject__iexact= "SCIENCE")

    return render(request,'onesubjectlistview.html',{'objects':objects})
