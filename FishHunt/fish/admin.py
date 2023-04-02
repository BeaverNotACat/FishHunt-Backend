from django.contrib import admin
from fish.models import Fish


@admin.register(Fish)
class TeamAdmin(admin.ModelAdmin):
    model = Fish

