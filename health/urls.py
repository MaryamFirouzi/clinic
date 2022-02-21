


from os import name
from django.contrib import admin
from django.urls import path
from health import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('clinic/<int:pk>', views.clinic, name='clinic_detail'),
    path('blog/', views.blog, name='blog'),
]
