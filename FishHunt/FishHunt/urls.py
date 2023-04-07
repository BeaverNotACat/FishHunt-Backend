from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from django.conf.urls.static import static

from FishHunt.settings import MEDIA_URL, MEDIA_ROOT
from fish.views import FishesViewSet
from classification.views import ValidateFishViewSet


router = routers.DefaultRouter()
router.register('fishes_list', FishesViewSet, basename='fishes_list')
router.register('validate_fish', ValidateFishViewSet, basename='validate_fish')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

