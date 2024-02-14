from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import * 
from django.http import HttpResponse


def create_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}
    if request.method=="POST":
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['sname']
            sp=SFDO.cleaned_data['sprinciple']
            sl=SFDO.cleaned_data['slocation']
            e=SFDO.cleaned_data['email']
            re=SFDO.cleaned_data['reenteremail']
            so=School.objects.get_or_create(sname=sn,sprinciple=sp,slocation=sl,email=e,reenteremail=re)[0]
            so.save()
            return HttpResponse('school is created')
        else:
            return HttpResponse('invalid data')
        
    return render(request,'create_school.html',d)