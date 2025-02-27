from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()  # 👈 Исправлено!
    serializer_class = ProductSerializer

