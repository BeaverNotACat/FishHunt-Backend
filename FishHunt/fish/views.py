from rest_framework import viewsets

from fish.models import Fish
from fish.serializers import FishSerializer
from fish.filters import FishIdFilter


class FishesViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    filter_class = FishIdFilter
    serializer_class = FishSerializer

