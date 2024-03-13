from rest_framework import serializers
from .models import (
    Cart,
    CartItem,
    Order,
    Favorite,
)


class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            "id",
            "user",
            "total_price",
            "creation_date",
            "update_date",
        ]

    def get_total_price(self, obj):
        cart_items = CartItem.objects.filter(cart=obj.id)
        total_price = 0
        for i in cart_items:
            total_price += i.tires.price * i.quantity
        return total_price


class CartItemSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CartItem
        fields = [
            "id",
            "cart",
            "user",
            "tires",
            "quantity",
        ]

    def validate(self, data):
        quantity = data["quantity"]
        tires = data["tires"]
        if quantity > tires.quantity:
            raise serializers.ValidationError(
                {"error": "The quantity of your request is less than the quantity of the product itself!"}
            )
        return data


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = [
            "id",
            "user",
            "tires",
        ]

    def validate(self, data):
        user = data.get("user")
        tires = data.get("tires")

        if Favorite.objects.filter(user=user, tires=tires).exists():
            raise serializers.ValidationError(
                {"error": "This tire is already in user's favorites list"}
            )

        return data
