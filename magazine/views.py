from email.mime import image
from django.shortcuts import render
from django.http import HttpResponse

from .forms import MagazineForm
from .models import Magazine
# Create your views here.
def update(request):
    if request.method =="POST":
        info = MagazineForm(request.POST,request.FILES)
        if info.is_valid():info.save()
        mags = Magazine.objects.all()
        return render(request,'index.html',{'mags':mags})
    else:
       return render(request,'update.html')
def home(request):
     mags = Magazine.objects.all()
     return render(request, 'index.html',{'mags':mags})
    
def about(request):
    return render(request,'about.html',{'name':'harshavardha bayavarapu'})




    