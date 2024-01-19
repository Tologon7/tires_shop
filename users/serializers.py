from rest_framework import serializers
from users.models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "email",
            "password",
            "message",
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def get_message(self, obj):
        return (
            "Verification message has been sent to your email, please verify your email"
        )


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ["token"]
