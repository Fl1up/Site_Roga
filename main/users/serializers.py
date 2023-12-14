from rest_framework import serializers

from main.users.models import User


class UserSerializer(serializers.ModelSerializer):
    # Сериализатор для пользователя
    class Meta:
        model = User
        fields = "__all__"
