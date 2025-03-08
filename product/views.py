from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
import logging
from rest_framework.views import APIView
from .models import Product, Category, Comment
from .serializers import ProductSerializerHomepage, CategoriesSerializer,  FavoriteProductListSerializer  , CommentSerializer# Подключаем сериализатор
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.permissions import AllowAny
from django.db.models import Count, Avg, F
from rest_framework import filters
from django.utils import timezone
from .filters import ProductFilter
from datetime import timedelta
from rest_framework.generics import ListAPIView
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
logger = logging.getLogger(__name__)
class HomepageView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerHomepage
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = ProductFilter

    def get(self, request, *args, **kwargs):
        logger.debug(f"Request filters: {request.GET}")  # Логируем параметры запроса
        response = super().get(request, *args, **kwargs)
        logger.debug(f"Response data: {response.data}")  # Логируем ответ
        return response

    def get(self, request, *args, **kwargs):
        logger.debug(f"Request filters: {request.GET}")  # Логируем параметры запроса
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['homepage'],
        operation_description="Этот эндпоинт возвращает данные для главной страницы, "
                              "включая популярные товары, товары на акциях и категорию акций.",
        responses={
            200: openapi.Response(
                description="Успешный ответ с данными для главной страницы",
                examples={
                    'application/json': {
                        "homepage": {
                            "popularProducts": [
                                {
                                    "productId": 1,
                                    "productImg": "https://example.com/images/product1.jpg",
                                    "productTitle": "Продукт 1",
                                    "average_rating": 4.5,
                                    "comments_count": 20,
                                    "price": "100.00",
                                    "seasonality": "summer",
                                    "is_favorite": True,
                                    "in_stock": 49
                                }
                            ],
                            "promotions": [
                                {
                                    "promotionId": 7,
                                    "promotionImg": "http://example.com/images/promotion1.jpg",
                                    "promotionTitle": "Скидка 20% на продукт",
                                    "promotionPrice": "80.00",
                                    "promotionEndTime": "3d 5h 10m 30s",
                                    "promotionCategory": [
                                        "Motor oil",
                                        "Автомасло"
                                    ]
                                }
                            ]
                        }
                    }
                },
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'homepage': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'popularProducts': openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(
                                        type=openapi.TYPE_OBJECT,
                                        properties={
                                            'productId': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID товара'),
                                            'productImg': openapi.Schema(type=openapi.TYPE_STRING, description='Изображение товара'),
                                            'productTitle': openapi.Schema(type=openapi.TYPE_STRING, description='Название товара'),
                                            'average_rating': openapi.Schema(type=openapi.TYPE_NUMBER, description='Средний рейтинг товара'),
                                            'comments_count': openapi.Schema(type=openapi.TYPE_INTEGER, description='Количество комментариев'),
                                            'price': openapi.Schema(type=openapi.TYPE_STRING, description='Цена товара'),
                                            'seasonality': openapi.Schema(type=openapi.TYPE_STRING, description='Сезонность товара'),
                                            'is_favorite': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Товар в избранном'),
                                            'in_stock': openapi.Schema(type=openapi.TYPE_INTEGER, description='Количество в складе ')
                                        }
                                    )
                                ),
                                'promotions': openapi.Schema(
                                    type=openapi.TYPE_ARRAY,
                                    items=openapi.Schema(
                                        type=openapi.TYPE_OBJECT,
                                        properties={
                                            'promotionId': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID акции'),
                                            'promotionImg': openapi.Schema(type=openapi.TYPE_STRING, description='Изображение акции'),
                                            'promotionTitle': openapi.Schema(type=openapi.TYPE_STRING, description='Название акции'),
                                            'promotionPrice': openapi.Schema(type=openapi.TYPE_STRING, description='Цена товара по акции'),
                                            'promotionEndTime': openapi.Schema(type=openapi.TYPE_STRING, description='Время окончания акции'),
                                            'promotionCategory': openapi.Schema(
                                                type=openapi.TYPE_ARRAY,
                                                items=openapi.Schema(type=openapi.TYPE_STRING, description='Категория акции')
                                            )
                                        }
                                    )
                                )
                            }
                        )
                    }
                )
            ),
            404: openapi.Response(
                description="Не найдено данных для главной страницы"
            ),
            500: openapi.Response(
                description="Ошибка сервера"
            ),
        }
    )
    def get(self, request):
        products = Product.objects.annotate(
            comments_count=Count('comment'),
            average_rating=Avg('comment__rating')
        ).filter(
            comments_count__gt=0,
            average_rating__isnull=False
        )

        sorted_products = products.order_by(
            F('average_rating').desc(nulls_last=True),
            '-comments_count'
        )

        popular_products = []
        for product in sorted_products[:4]:
            product_data = {
                "productId": product.id,
                "productImg": product.image.url,
                "productTitle": product.title,
                "average_rating": product.average_rating,
                "comments_count": product.comments_count,
                "price": str(product.price),
                "seasonality": product.seasonality,
                "is_favorite": product.is_favorite,
                "in_stock": product.in_stock,
            }
            popular_products.append(product_data)

        promotions = Product.objects.filter(
            promotion__isnull=False,
            promotion_end_date__gt=timezone.now()
        )

        promotion_data = []
        for product in promotions:
            if product.promotion_end_date:
                time_remaining = product.promotion_end_date - timezone.now()
                if time_remaining.total_seconds() <= 0:
                    promotion_end_time = "Акция завершена"
                else:
                    days_remaining = time_remaining.days
                    hours_remaining = time_remaining.seconds // 3600
                    minutes_remaining = (time_remaining.seconds % 3600) // 60
                    seconds_remaining = time_remaining.seconds % 60
                    promotion_end_time = f"{days_remaining}d {hours_remaining}h {minutes_remaining}m {seconds_remaining}s"
            else:
                promotion_end_time = "Not set"

            promotion_categories = product.promotion_category.all()
            promotion_category_data = [
                category.value for category in promotion_categories
            ]

            promotion_data.append({
                "promotionId": product.id,
                "promotionImg": product.image.url,
                "promotionTitle": product.title,
                "promotionPrice": str(product.promotion),
                "promotionEndTime": promotion_end_time,
                "promotionCategory": promotion_category_data,
            })

        homepage_data = {
            "homepage": {
                "popularProducts": popular_products,
                "promotions": promotion_data
            }
        }

        return Response(homepage_data)
class CategoriesListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            # Возвращаем label и value
            return Response({'label': category.label, 'value': category.value}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FavoriteProduct(APIView):
    """
    Получение списка избранных продуктов и обновление статуса "избранного".
    """

    def get(self, request):
        # Получаем все избранные продукты
        queryset = Product.objects.filter(is_favorite=True)
        serializer = FavoriteProductListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Получаем данные из POST-запроса
        product_id = request.data.get('product_Id')
        is_favorite = request.data.get('is_favorite')  # Получаем is_favorite, если оно есть

        if product_id is None:
            return Response({"detail": "Product ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Получаем продукт по ID
        product = get_object_or_404(Product, id=product_id)

        # Если is_favorite передано в запросе, обновляем статус
        if is_favorite is not None:
            product.is_favorite = is_favorite
        else:
            # Если is_favorite не передано, меняем его на противоположное
            product.is_favorite = not product.is_favorite

        # Сохраняем продукт с обновленным значением is_favorite
        product.save()

        # Сериализуем обновленный продукт
        serializer = FavoriteProductListSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentCreateView(generics.CreateAPIView):
    """
    Создание комментария с указанием product.
    """
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        product_id = self.request.data.get("product")  # Теперь берем `product` вместо `product_id`
        try:
            product = Product.objects.get(id=product_id)  # Проверяем, существует ли продукт
        except Product.DoesNotExist:
            raise ValidationError({"product": "Продукт с таким ID не найден."})

        serializer.save(product=product)  # Привязываем комментарий к продукту


def round_to_half(value):

    return round(value * 2) / 2


@receiver(post_save, sender=Comment)
@receiver(post_delete, sender=Comment)
def update_product_rating(sender, instance, **kwargs):
    """Этот метод теперь просто триггерит обновление кеша, если нужно, но ничего не сохраняет в БД."""
    product = instance.product

class ProductCommentListView(generics.ListAPIView):
    """
    Получение всех комментариев к конкретному продукту.
    """
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        return Comment.objects.filter(product_id=product_id)
