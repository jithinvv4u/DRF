from pydoc import resolve
from django.http import response
from django.shortcuts import render
from app1.models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .pagination import CustomerPageNumberPagination
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

class CompayModelViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
class CustomerModelViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    pagination_class=CustomerPageNumberPagination
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    
# @api_view(['GET', 'POST'])
# def customer_list(request):
#     if request.method=='GET':
#         customer=Customer.objects.all()
#         serializer=CustomerSerializer(customer,many=True)
#         return response(serializer.data)
    
#     elif request.method=='POST':
#         serializer=CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response(serializer.data,status.HTTP_201_CREATED)
#         return response(serializer.errors,status.HTTP_400_BAD_REQUEST)
