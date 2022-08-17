from rest_framework import serializers
from .models import *

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        extra_kwargs = {
            'username': { 'required': True, 'allow_blank': False },
            'email': { 'required': True, 'allow_blank': False },
            'password': { 'required': True, 'allow_blank': False, 'min_length': 6 },
        }
