# filters.py
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
        fields = ['manufacturer', 'model', 'generation', 'modification', 'body_type']
