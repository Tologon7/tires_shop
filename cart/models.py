from django.db import models
from tires.models import Tires
from users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import User


class Cart(models.Model):
    total_price = models.FloatField(default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)


post_save.connect(create_user_cart, sender=User)


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tires = models.ForeignKey(Tires, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"cart: {self.cart}, tires: {self.tires}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_price = models.FloatField(default=1)

