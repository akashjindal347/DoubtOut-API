from django.shortcuts import render
from .forms import SubjectForm
from .models import Subject
# Create your views here.
def SubjectView(request):
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request,'createsubject.html',{'form':form})
