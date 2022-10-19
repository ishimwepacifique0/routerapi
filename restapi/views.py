from rest_framework import viewsets
from .serializers import Workrouter
from .models import *


class Hero(viewsets.ModelViewSet):
    queryset = Detail.objects.all().order_by('name')
    serializer_class = Workrouter