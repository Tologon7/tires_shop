from rest_framework import generics
from .models import *
from .serializers import *


class CartItemList(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


class Cart(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class Order(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class Favorite(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

