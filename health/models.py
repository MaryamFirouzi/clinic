from contextlib import closing
from distutils.command.upload import upload
import email
from email.headerregistry import Address
from pydoc import describe
from pyexpat import model
from random import choices
from tkinter import CASCADE
from tkinter.tix import DisplayStyle
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
import datetime as dt
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Doctor(models.Model):
    #clinic=models.ManyToManyField(Clinic)
    name= models.CharField(max_length=30 , null=True)
    image=models.ImageField(upload_to='doctor',null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.name

      
class Clinic(models.Model):
    name=models.CharField(max_length=120,null=True)
    top_img=models.ImageField(upload_to='img')   
    phone=models.CharField(max_length=15,null=True)
    Address=models.TextField(null=True)
    doctor=models.ManyToManyField(Doctor)
    description_head=RichTextField(null=True, max_length=50) 
    description=RichTextField(null=True) 
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("clinic_detail", args=(self.id,) )   




class Day(models.Model):
    days=(('شنبه','شنبه'),
          ('یکشنبه','یکشنبه'),
          ('دوشنبه','د.شنبه'),
          ('دوشنبه','دوشنبه'),
          ('سه شنبه','سه شنبه'),
          ('چهارشنبه','چهارشنبه'),
          ('پنجشنبه','پنجشنبه'),
          ('جمعه','جمعه') )
      
    clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE,null=True)
    opening_day=models.CharField(max_length=10,choices=days,null=True)
     
    def __str__(self):
        return self.opening_day

class Hours(models.Model):
    day=models.ForeignKey(Day,on_delete=models.CASCADE,null=True)
    hours=[(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]
    opening_hour=models.TimeField(null=True,choices=hours)
    closing_hour=models.TimeField(null=True,choices=hours)

class Blog(models.Model):
    head=RichTextField(null=True)  
    describtion=RichTextField(null=True)  

    def __str__(self):
        return self.head 

    def get_absolute_url(self):
        return reverse("blog",args=[self.id] )     

class Comment(models.Model):
    fullname=models.TextField(max_length=50,null=True)
    e_mail=models.EmailField( max_length=254,null=True)     
    description=RichTextField() 
    def __str__(self):
        return self.fullname  

class Clinic_info(models.Model): 
    days=(('شنبه','شنبه'),
          ('یکشنبه','یکشنبه'),
          ('دوشنبه','د.شنبه'),
          ('دوشنبه','دوشنبه'),
          ('سه شنبه','سه شنبه'),
          ('چهارشنبه','چهارشنبه'),
          ('پنجشنبه','پنجشنبه'),
          ('جمعه','جمعه') )
    name=models.CharField(max_length=50,null=True)
    star_day=models.CharField(max_length=10,choices=days,null=True)
    end_day=models.CharField(max_length=10,choices=days,null=True)
    hours=[(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]
    opening_hour=models.TimeField(null=True,choices=hours)
    closing_hour=models.TimeField(null=True,choices=hours)  
    phone=models.CharField(max_length=20,null=True)    
    address=models.CharField(max_length=120,null=True)  
    img=models.ImageField(upload_to='img', null=True)
    slider_img=models.ImageField(upload_to='img', null=True)
    top_image=models.ImageField(upload_to='img', null=True)

    def __str__(self):
        return str(self.name)