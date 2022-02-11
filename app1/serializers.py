from dataclasses import fields
from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields=['cmp_name','location']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Customer
        fields=['name','company','age','place']