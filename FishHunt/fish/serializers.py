from rest_framework import serializers

from fish.models import Fish


class FishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fish
        fields = ['id' ,'name', 'description']
