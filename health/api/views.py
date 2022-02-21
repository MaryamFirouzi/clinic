from pdb import Pdb
from django.db import models
from django.shortcuts import render
from django.http import JsonResponse, response
from health.models import Clinic
from rest_framework.response import Response
from rest_framework.decorators import api_view
from health.api.serializers import clinicsserializers


        
@api_view(['GET'])
def clinic(request):
    clinic=Clinic.objects.all()
    serializer= clinicsserializers(clinic , many=True ,context=request.GET)
    return Response(serializer.data)

@api_view(['GET'])
def clinic_detail(request,pk):
    clinic=Clinic.objects.get(pk=pk)
    serializer= clinicsserializers(clinic  ,context=request.GET)
    return Response(serializer.data)    