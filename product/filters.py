import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    manufacturer = django_filters.CharFilter(field_name="manufacturer", lookup_expr="icontains")
    model = django_filters.CharFilter(field_name="model", lookup_expr="icontains")
    generation = django_filters.CharFilter(field_name="generation", lookup_expr="icontains")
    modification = django_filters.CharFilter(field_name="modification", lookup_expr="icontains")
    body_type = django_filters.CharFilter(field_name="body_type", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = {
            'manufacturer': ['exact', 'icontains'],
            'model': ['exact', 'icontains'],
            'generation': ['exact', 'icontains'],
            'modification': ['exact', 'icontains'],
            'body_type': ['exact', 'icontains'],
            'price': ['gte', 'lte'],  # Добавим фильтр по цене (от/до)
        }
