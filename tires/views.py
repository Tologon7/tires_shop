from django.shortcuts import render
from rest_framework import generics
from tires.serializers import TiresSerializer
from tires.models import Tires


class TiresListAPIView(generics.ListAPIView):
    queryset = Tires.objects.all()
    serializer_class = TiresSerializer

