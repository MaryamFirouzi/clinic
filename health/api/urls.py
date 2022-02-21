from django.urls import path
from health.api import views

urlpatterns = [
    
    path('clinic/', views.clinic),
    path('clinic/<int:pk>', views.clinic_detail),
]