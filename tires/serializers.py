from rest_framework import serializers
from tires.models import Tires


class TiresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tires
        fields = '__all__'
