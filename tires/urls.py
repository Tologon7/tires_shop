from django.urls import path
from .views import TiresListAPIView

urlpatterns = [
    path('list/', TiresListAPIView.as_view(), name='tires-list'),

]
