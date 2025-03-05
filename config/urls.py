from django.contrib import admin
from django.urls import path, include
from config import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Создаем схему Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API для работы с товарами и акциями",
        default_version='v1',
        description="Описание API для работы с товарами и их акциями",
        terms_of_service="https://www.your-terms-of-service.com",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include("product.urls")),  # Ваши другие URL-ы

    # URL для доступа к Swagger-документации
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),  # Добавляем UI Swagger
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # Для получения схемы в формате JSON
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Добавляем UI ReDoc (альтернатива Swagger)
]

# Статические файлы
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



