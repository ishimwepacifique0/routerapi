from dataclasses import fields
from rest_framework import serializers
from . models import *

class Workrouter(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detail
        fields = ('name','age','phonenumber','email')
