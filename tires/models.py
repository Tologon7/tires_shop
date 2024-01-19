from django.db import models


class Width(models.Model):
    width = models.FloatField()

    def __int__(self):
        return self.width


class Profile(models.Model):
    profile = models.FloatField()

    def __int__(self):
        return self.profile


class Diameter(models.Model):
    diameter = models.FloatField()

    def __int__(self):
        return self.diameter


class CarType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Seasonality(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Generator(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SpeedIndex(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class LoadIndex(models.Model):
    load = models.IntegerField()

    def __int__(self):
        return self.load


class FuelEconomy(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class GripOnWetSurfaces(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class ExternalNoiseLevel(models.Model):
    decibel = models.IntegerField()

    def __int__(self):
        return self.decibel


class Tires(models.Model):
    width = models.ForeignKey('Width', on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    diameter = models.ForeignKey('Diameter', on_delete=models.CASCADE)
    price = models.IntegerField()
    car_type = models.ForeignKey('CarType', on_delete=models.CASCADE, null=True)
    seasonality = models.ForeignKey('Seasonality', on_delete=models.CASCADE, null=True)
    state = models.BooleanField(default=False)
    generator = models.ForeignKey('Generator', on_delete=models.PROTECT, null=True)
    discount = models.BooleanField(default=False)
    runflat = models.BooleanField(default=False)
    offroad = models.BooleanField(default=False)
    speed_index = models.ForeignKey('SpeedIndex', on_delete=models.CASCADE, null=True)
    load_index = models.ForeignKey('LoadIndex', on_delete=models.CASCADE, blank=True, null=True)
    fuel_economy = models.ForeignKey('FuelEconomy', on_delete=models.CASCADE, null=True)
    grip_on_wet_surfaces = models.ForeignKey('GripOnWetSurfaces', on_delete=models.CASCADE, null=True)
    external_noise_level = models.ForeignKey('ExternalNoiseLevel', on_delete=models.CASCADE, null=True)
    set = models.BooleanField()
    in_stock = models.BooleanField()
