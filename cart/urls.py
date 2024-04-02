from django.urls import path
from .views import *


urlpatterns = [
    path('cart/', Cart.as_view()),
    path('cart-item/', CartItemList.as_view(), name='cart-list'),
    path('cart-item/<int:cart_id>/', CartItemListId.as_view(), name='cart-id'),
    path('cart-item/edit/<int:pk>/', CartItemRetrieveUpdateDestroyAPIView.as_view()),


]
