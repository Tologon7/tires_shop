from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError


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
        for item in cart_items:
            if item.tires and hasattr(item.tires, 'price'):
                total_price += item.tires.price * item.quantity
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
        user = data['user']

        if quantity > tires.quantity:
            raise serializers.ValidationError(
                {"error": "The quantity of your request is less than the quantity of the product itself!"}
            )

        if CartItem.objects.filter(tires=tires, cart__user=user).exists():
            raise serializers.ValidationError(
                {"error": "This product is already in the cart"}
            )

        return data

    def validate_cart(self, value):
        user = self.context['request'].user
        if user.is_authenticated and user.cart.id != value.id:
            raise ValidationError("You can only add items to your own cart.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


