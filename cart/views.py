from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied


class CartItemList(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


class CartItemListId(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user_cart_id = self.request.user.cart.id
        return CartItem.objects.filter(cart_id=user_cart_id)

    def perform_create(self, serializer):
        user_cart_id = self.request.user.cart.id
        if serializer.validated_data['cart_id'] != user_cart_id:
            raise PermissionDenied("You can only add items to your own cart.")
        serializer.save()


class CartItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    @swagger_auto_schema(
        tags=['Cart'],
        operation_description="Этот ендпоинт предоставляет "
                              "возможность редактировать "
                              "текущий товар в корзине. ",
    )

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return CartItem.objects.filter(id=self.kwargs["pk"])


class Cart(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class Order(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()



