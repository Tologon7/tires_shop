from rest_framework import serializers
from .models import *
from .utils import *


class TiresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tires
        fields = [
            'id',
            'title',
            'profile',
            'price',
            'promotion',
            'in_stock',
            'state'
        ]


class TiresidSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # width = serializers.PrimaryKeyRelatedField(queryset=Width.objects.all())
    # profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    # diameter = serializers.PrimaryKeyRelatedField(queryset=Diameter.objects.all())
    # car_type = serializers.PrimaryKeyRelatedField(queryset=CarType.objects.all())
    # seasonality = serializers.PrimaryKeyRelatedField(queryset=Seasonality.objects.all())
    # manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all())
    # speed_index = serializers.PrimaryKeyRelatedField(queryset=SpeedIndex.objects.all())
    # load_index = serializers.PrimaryKeyRelatedField(source='load_index.title', queryset=LoadIndex.objects.all())
    # fuel_economy = serializers.PrimaryKeyRelatedField(source='fuel_economy.title', queryset=FuelEconomy.objects.all())
    # grip_on_wet_surfaces = serializers.PrimaryKeyRelatedField(source='grip_on_wet_surfaces.title', queryset=GripOnWetSurfaces.objects.all())
    # external_noise_level = serializers.PrimaryKeyRelatedField(source='external_noise_level.title', queryset=ExternalNoiseLevel.objects.all())
    # model = serializers.PrimaryKeyRelatedField(source='model.title', queryset=Model.objects.all())
    # load_index_for_dual = serializers.PrimaryKeyRelatedField(source='load_index_for_dual.title', queryset=LoadIndexForDual.objects.all())

    class Meta:
        model = Tires
        fields = '__all__'


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# class Reviewsserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reviews
#         fields = '__all__'
#
#     def create(self, validated_data):
#         tir_id = self.context["tir_id"]
#         user_id = self.context["user_id"]
#         rating = Reviews.objects.create(tir_id=tir_id, user_id=user_id, **self.validated_data)
#         return rating


class Reviewsserializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

    def create(self, validated_data):
        tir_id = self.context.get("tir_id")
        user_id = self.context.get("user_id")
        review = Reviews.objects.create(tires_id=tir_id, user_id=user_id, **validated_data)
        return review


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
