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


# class TiresidSerializer(serializers.ModelSerializer):
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     width = serializers.PrimaryKeyRelatedField(queryset=Width.objects.all())
#     profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
#     diameter = serializers.PrimaryKeyRelatedField(queryset=Diameter.objects.all())
#     car_type = serializers.PrimaryKeyRelatedField(queryset=CarType.objects.all())
#     seasonality = serializers.PrimaryKeyRelatedField(queryset=Seasonality.objects.all())
#     manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all())
#     speed_index = serializers.PrimaryKeyRelatedField(queryset=SpeedIndex.objects.all())
#     load_index = serializers.PrimaryKeyRelatedField(queryset=LoadIndex.objects.all())
#     fuel_economy = serializers.PrimaryKeyRelatedField(queryset=FuelEconomy.objects.all())
#     grip_on_wet_surfaces = serializers.PrimaryKeyRelatedField(queryset=GripOnWetSurfaces.objects.all())
#     external_noise_level = serializers.PrimaryKeyRelatedField(queryset=ExternalNoiseLevel.objects.all())
#     model = serializers.StringRelatedField()
#     load_index_for_dual = serializers.PrimaryKeyRelatedField(queryset=LoadIndexForDual.objects.all())
#
#     class Meta:
#         model = Tires
#         fields = "__all__"


class TiresCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tires
        fields = [
            'id',
            'title',
            'category',
            'width',
            'profile',
            'diameter',
            'price',
            'promotion',
            'quantity',
            'car_type',
            'seasonality',
            'state',
            'manufacturer',
            'discount',
            'runflat',
            'offroad',
            'speed_index',
            'load_index',
            'fuel_economy',
            'grip_on_wet_surfaces',
            'external_noise_level',
            'set',
            'in_stock',
            'model',
            'load_index_for_dual'

        ]



class TiresidSerializer(serializers.ModelSerializer):
    # title = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    width = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()
    diameter = serializers.SerializerMethodField()
    # price = serializers.SerializerMethodField()
    # promotion = serializers.SerializerMethodField()
    # quantity = serializers.SerializerMethodField()
    car_type = serializers.SerializerMethodField()
    seasonality = serializers.SerializerMethodField()
    # state = serializers.SerializerMethodField()
    manufacturer = serializers.SerializerMethodField()
    # discount = serializers.SerializerMethodField()
    # runflat = serializers.SerializerMethodField()
    # offroad = serializers.SerializerMethodField()
    speed_index = serializers.SerializerMethodField()
    load_index = serializers.SerializerMethodField()
    fuel_economy = serializers.SerializerMethodField()
    grip_on_wet_surfaces = serializers.SerializerMethodField()
    external_noise_level = serializers.SerializerMethodField()
    # set = serializers.SerializerMethodField()
    # in_stock = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()
    load_index_for_dual = serializers.SerializerMethodField()

    class Meta:
        model = Tires
        # fields = '__all__'
        fields = [
            'id',
            'title',
            'category',
            'width',
            'profile',
            'diameter',
            'price',
            'promotion',
            'quantity',
            'car_type',
            'seasonality',
            'state',
            'manufacturer',
            'discount',
            'runflat',
            'offroad',
            'speed_index',
            'load_index',
            'fuel_economy',
            'grip_on_wet_surfaces',
            'external_noise_level',
            'set',
            'in_stock',
            'model',
            'load_index_for_dual'

        ]

    # def get_title(self, obj):
    #     return obj.title

    def get_category(self, obj):
        return obj.category.title

    def get_width(self, obj):
        return obj.width.title

    def get_profile(self, obj):
        return obj.profile.title

    def get_diameter(self, obj):
        return obj.diameter.title

    # def get_price(self, obj):
    #     return obj.price

    # def get_promotion(self, obj):
    #     return obj.promotion

    # def get_quantity(self, obj):
    #     return obj.quantity

    def get_car_type(self, obj):
        return obj.car_type.title

    def get_seasonality(self, obj):
        return obj.seasonality.title

    # def get_state(self, obj):
    #     return obj.state

    def get_manufacturer(self, obj):
        return obj.manufacturer.title

    # def get_discount(self, obj):
    #     return obj.discount
    #
    # def get_runflat(self, obj):
    #     return obj.runflat
    #
    # def get_offroad(self, obj):
    #     return obj.offroad

    def get_speed_index(self, obj):
        return obj.speed_index.title

    def get_load_index(self, obj):
        return obj.load_index.title

    def get_fuel_economy(self, obj):
        return obj.fuel_economy.title

    def get_grip_on_wet_surfaces(self, obj):
        return obj.grip_on_wet_surfaces.title

    def get_external_noise_level(self, obj):
        return obj.external_noise_level.title

    # def get_set(self, obj):
    #     return obj.set
    #
    # def get_in_stock(self, obj):
    #     return obj.in_stock

    def get_model(self, obj):
        return obj.model.title

    def get_load_index_for_dual(self, obj):
        return obj.load_index_for_dual.title


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Reviewsserializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = [
            'id'
            'user',
            'tires',
            'comment',
            'rating'
        ]


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
