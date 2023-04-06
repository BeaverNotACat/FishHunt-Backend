from rest_framework import serializers

from drf_extra_fields.fields import Base64ImageField


class ValidateRequestSerializer(serializers.Serializer):
    fish_id = serializers.IntegerField()
    image = Base64ImageField()

