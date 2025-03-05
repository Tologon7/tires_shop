
from rest_framework import serializers
from .models import Product, Category, Comment


# Словарь для перевода с русского на английский
RUS_TO_ENG = {
    'Автомобильные шины': 'Car tires',
    'Грузовые машины': 'Trucks',
    'сельскохозяйственные шины': 'Agricultural tires',
    'Дорожно строительный': 'Road construction',
    'Аксессуары для шин, дисков и шиномонтажа': 'Tire, wheel, and tire service accessories',
    'Аккумуляторы': 'Batteries',
    'Автомасло': 'Motor oil',
    'Автоэлектроника': 'Car electronics',
    'Автохимия и автокосметика': 'Auto chemicals and car cosmetics',
    'Внешний декор, тюнинг, защита': 'Exterior decor, tuning, protection',
    'Инструменты и техническая помощь': 'Tools and technical assistance',
    'Компрессоры': 'Compressors',
}


class CategoriesSerializer(serializers.ModelSerializer):
    label = serializers.CharField()
    value = serializers.CharField(required=False)  # Делаем value необязательным

    class Meta:
        model = Category
        fields = ['id','label', 'value']

    def create(self, validated_data):
        if 'value' not in validated_data or not validated_data['value']:
            label = validated_data['label']
            # Переводим label на английский
            validated_data['value'] = RUS_TO_ENG.get(label, label)  # Если нет перевода, оставляем label как есть
        return super().create(validated_data)



class ProductSerializerHomepage(serializers.ModelSerializer):
    product_Id = serializers.IntegerField(source='id')  # Переименовываем 'id' в 'productId'
    average_rating = serializers.SerializerMethodField()
    comments_count = serializers.IntegerField(source="comment_set.count", read_only=True)
    image = serializers.SerializerMethodField()
    set = serializers.SerializerMethodField()
    in_stock = serializers.SerializerMethodField()
    promotion_category = CategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_Id','image','seasonality', "average_rating", "comments_count", 'title',  "set",  # Показываем только если True
            "in_stock", 'price', 'is_favorite', 'promotion_category', ]

    def get_image(self, obj):
        if obj.image:
            return obj.image.url  # Возвращаем URL изображения, если оно есть
        return None
    def get_comments_count(self, obj):
        return obj.comments.count()  # Количество комментариев

    def get_average_rating(self, obj):
        return obj.average_rating  # Средний рейтинг

    def get_set(self, obj):
        if obj.set:
            return True
        return None  # Если False, то ничего не показываем

    def get_in_stock(self, obj):
        if obj.in_stock:
            return True
        return None  # Если False, то ничего не показываем
    def get_average_rating(self, obj):
        """Вычисляет средний рейтинг продукта на лету."""
        comments = obj.comment_set.all()
        from .views import round_to_half
        if not comments:
            return 0.0
        total_rating = sum(comment.rating for comment in comments)
        return round_to_half(total_rating / len(comments))




class FavoriteProductListSerializer(serializers.ModelSerializer):
    product_Id = serializers.IntegerField(source='id')  # Переименовываем 'id' в 'productId'

    class Meta:
        model = Product
        fields = ['product_Id', 'image', 'price', 'seasonality', 'title', 'inStock', 'is_favorite']

class CommentSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())


    class Meta:
        model = Comment
        fields = ['id', 'product', 'comment', 'rating', 'created_at']

    def validate_product(self, value):
        if isinstance(value, Product):  # Если передали объект, берем его ID
            value = value.id
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Такого продукта не существует")
        return value
