from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from FishHunt.settings import MEDIA_URL, MEDIA_ROOT, DEBUG
from fish.views import FishesViewSet
from classification.views import ValidateFishViewSet


router = routers.DefaultRouter()
router.register('fishes_list', FishesViewSet, basename='fishes_list')
router.register('validate_fish', ValidateFishViewSet, basename='validate_fish')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()

