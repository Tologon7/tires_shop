from django.urls import path
from .views import CartItemList
from .views import Favorite
from .views import Cart


urlpatterns = [
    path('cart/', Cart.as_view()),
    path('cart-item/', CartItemList.as_view(), name='cart-list'),
    path('favorite/', Favorite.as_view(), name='favorite-list')
]