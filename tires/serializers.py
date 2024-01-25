from rest_framework import serializers
from .models import *


class TiresSerializer(serializers.ModelSerializer):

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