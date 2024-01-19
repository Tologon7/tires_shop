from django.db import models

from django.db import models
from django.db.models import Sum

from users.managers import SuperUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, null=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = SuperUser()

    def __str__(self):
        return self.username


class Points(models.Model):
    points = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.points


class FeedBack(models.Model):
    RATE = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(choices=RATE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
