from django.db import models
from tires.models import Tires
from users.models import User


class Cart(models.Model):
    total_price = models.FloatField(default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tires = models.ForeignKey(Tires, on_delete=models.SET_NULL,null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL,null=True,related_name="cart_item")
    quantity = models.IntegerField(default=1)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"user: {self.user}, cart: {self.cart}, tires: {self.tires}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_price = models.FloatField(default=1)


class Favorite(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tires = models.ForeignKey(Tires, on_delete=models.CASCADE)

    def __str__(self):
        return f"user: {self.user}, tires: {self.tires}"


