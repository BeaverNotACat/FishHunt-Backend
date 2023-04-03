import os
import base64

from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from fish.models import Fish


class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ['id' ,'name', 'description', 'image']

