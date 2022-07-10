from django.shortcuts import render
from rest_framework import generics
from women.models import Women

# Create your views here.
from .serializer import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
