import django_filters
from .models import Item

class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Item
        fields = ['name', 'description']