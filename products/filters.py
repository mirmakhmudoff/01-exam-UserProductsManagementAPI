import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'created_by': ['exact'],
            'price': ['gte', 'lte'],
        }
