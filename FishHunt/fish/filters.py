import django_filters
from fish.models import Fish


class FishIdFilter(django_filters.FilterSet):
     blog_post_id = django_filters.NumberFilter(name = 'id')
     class Meta:
          model = Fish
          fields = ['id']
