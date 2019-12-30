from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .forms import  StudentForm
from .models import Student

def index(request):
    students = Student.objects.all()
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students':students,
        'form':form,
    }
    return render(request,'index.html',context=context)