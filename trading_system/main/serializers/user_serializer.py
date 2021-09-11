from rest_framework import serializers
from django.contrib.auth import get_user_model
from main.models import Verification
from random import randint


class UserSerializer(serializers.ModelSerializer):
    verif_code = serializers.StringRelatedField()
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', "verif_code","email")
        extra_kwargs = {
            'password': {'write_only': True},
            "verif_code": {"read_only": True}
            }

    def create(self, validated_data):
        password = validated_data.pop('password')
        verif_code = randint(10000,99999)
        #send_sms(verif_code)
        user = get_user_model().objects.create_user(
            password=password,
            is_active=False,
            **validated_data
            )
        Verification.objects.create(user=user,verification_code=verif_code)
        return user