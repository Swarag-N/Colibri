from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 

from colibri.models import Colibri
from colibri.serializers import ColibriSerializer
# Create your views here.
class ColibriViewSet(ModelViewSet):
    queryset = Colibri.objects.all()
    serializer_class = ColibriSerializer
    # permission_classes = [IsAuthenticated]
    