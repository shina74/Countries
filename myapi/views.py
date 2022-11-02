from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CountrySerializer
from .models import Country


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer
