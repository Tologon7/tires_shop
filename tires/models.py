from django.db import models
# from django.contrib.auth.models import User
from users.models import User
from rest_framework.authtoken.models import Token


class Width(models.Model):
    title = models.IntegerField()

    def __str__(self):
        return f"{self.title}"


class Profile(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title}'


class Diameter(models.Model):
    title = models.FloatField()

    def __str__(self):
        return f'{self.title}'


class CarType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class Seasonality(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class Manufacturer(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class SpeedIndex(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class LoadIndex(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class FuelEconomy(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class GripOnWetSurfaces(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class LoadIndexForDual(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.title}'


class Model(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'


class ExternalNoiseLevel(models.Model):
    title = models.IntegerField()

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Tires(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    width = models.ForeignKey('Width', on_delete=models.CASCADE, blank=True, null=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, blank=True, null=True)
    diameter = models.ForeignKey('Diameter', on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    promotion = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    car_type = models.ForeignKey('CarType', on_delete=models.CASCADE,  blank=True, null=True)
    seasonality = models.ForeignKey('Seasonality', on_delete=models.CASCADE,  blank=True, null=True)
    state = models.BooleanField(default=False, blank=True, null=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT, blank=True, null=True)
    discount = models.BooleanField(default=False, blank=True,null=True)
    runflat = models.BooleanField(default=False, blank=True,null=True)
    offroad = models.BooleanField(default=False, blank=True,null=True)
    speed_index = models.ForeignKey('SpeedIndex', on_delete=models.CASCADE,  blank=True, null=True)
    load_index = models.ForeignKey('LoadIndex', on_delete=models.CASCADE, blank=True, null=True)
    fuel_economy = models.ForeignKey('FuelEconomy', on_delete=models.CASCADE, blank=True, null=True)
    grip_on_wet_surfaces = models.ForeignKey('GripOnWetSurfaces', on_delete=models.CASCADE, blank=True, null=True)
    external_noise_level = models.ForeignKey('ExternalNoiseLevel', on_delete=models.CASCADE, blank=True, null=True)
    set = models.BooleanField(blank=True, null=True)
    in_stock = models.BooleanField(blank=True, null=True)
    model = models.ForeignKey('Model', on_delete=models.CASCADE,  blank=True, null=True)
    load_index_for_dual = models.ForeignKey('LoadIndexForDual', on_delete=models.CASCADE,  blank=True, null=True)
    # reviews = models.ForeignKey('Reviews', on_delete=models.CASCADE,  blank=True, null=True)

    def __str__(self):
        return str(self.title)




# class Reviews(models.Model):
#     tires = models.ForeignKey(Tires, on_delete=models.CASCADE, related_name='reviews')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment = models.TextField(blank=True,null=True,)
#     rating = models.PositiveIntegerField(choices=((1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')))
#
#     class Meta:
#         unique_together = ('tires', 'user')
#         user = User.objects.get(username='username')
#         token, created = Token.objects.get_or_create(user=user)
#
#     def __str__(self):
#         return f"{self.user}'s - {self.rating} - star rating for {self.tires}"


class Reviews(models.Model):
    tires = models.ForeignKey('Tires', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(choices=((1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')))

    class Meta:
        unique_together = ('tires', 'user')
        ordering = ['-id']  # Example: Ordering by the primary key in descending order

    def __str__(self):
        return f"{self.user}'s - {self.rating} - star rating for {self.tires}"
