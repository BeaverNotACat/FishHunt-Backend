import os
import base64

from django.db.models.query import QuerySet
from convert_to_queryset import list_to_queryset

from fish.models import Fish


def convert_queryset_image_into_base64(queryset: QuerySet[Fish]) -> QuerySet:
    fishes: tuple[Fish] = [fish for fish in queryset]
    images: tuple[bytearray] = tuple(
            bytearray(os.open(str(fish.image), os.O_RDONLY )) for fish in fishes)
    
    for x in range(len(fishes)):
        fishes[x].image = base64.b64encode(images[x])
    return list_to_queryset(Fish ,fishes)
