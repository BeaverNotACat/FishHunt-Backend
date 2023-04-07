from django.db import models

from FishHunt.settings import MEDIA_PATH


class Fish(models.Model):
    """A fish information"""
    name = models.CharField(max_length=40)
    description = models.TextField()
    model_label = models.IntegerField()
    image = models.ImageField(upload_to=MEDIA_PATH)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "fish"
        verbose_name_plural = "fishes"
