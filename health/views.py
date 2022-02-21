from xml.etree.ElementTree import Comment
from django.shortcuts import render

from health.models import Blog, Clinic, Clinic_info , Day , Comment 

# Create your views here.
def home(request):
    ctx={
        'clinics':Clinic.objects.all() ,
        'clinic_infos':Clinic_info.objects.first()
    }
   
    return render(request , 'home.html',ctx)

def clinic(request , pk):
    ctx={
        'clinic':Clinic.objects.get(pk=pk)     
    }
    return render(request , 'clinic_detail.html',ctx)    


def blog(request):
    ctx={
        "blog":Blog.objects.all(),
        "comment":Comment.objects.all()
    }
    return render(request , 'blog.html',ctx)        