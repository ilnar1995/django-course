from django.db import models
from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics
from .models import Women

# Create your views here.
from .serializer import WomenSerializer


class WomenAPIView(generics.ListAPIView):
    #queryset = Women.objects.all().annotate(test=Count('id'))
    queryset = Women.objects.filter(id=1).annotate(test=Count('id'))
    #print(queryset.get().__dict__)
    #print(dir(queryset.get()))
    serializer_class = WomenSerializer
