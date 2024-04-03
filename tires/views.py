from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from tires.serializers import (
    TiresSerializer,
    Categoryserializer,
    Reviewsserializer,
    TiresidSerializer,
    FavoriteSerializer
)

from rest_framework import generics
from .models import *

from rest_framework import status
from django.db.models import Count
from tires.models import (
    Tires,
    Category,
    Reviews,
    Favorite
)


class Categoryviewid(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer

    def get_queryset(self, *args, **kwargs):
        return Category.objects.filter(id=self.kwargs["cat_id"])


class Categoryview(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer


class Tiresview(generics.ListCreateAPIView):
    queryset = Tires.objects.all()
    serializer_class = TiresSerializer


class Tiresviewid(generics.ListCreateAPIView):
    queryset = Tires.objects.all()
    serializer_class = TiresidSerializer

    @swagger_auto_schema(
        tags=['Tires'],
        operation_description="Этот ендпоинт предоставляет "
                              "возможность посмотреть детально "
                              "текущий товар по id. ",
    )
    def get_queryset(self, *args, **kwargs):
        return Tires.objects.filter(id=self.kwargs["tir_id"])


# class Reviewsview(generics.ListCreateAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = Reviewsserializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self, *args, **kwargs):
#         return Reviews.objects.filter(id=self.kwargs["rev_id"])
#
#     def get_serializer_context(self):
#         user_id = self.request.user.id
#         tir_id = self.kwargs["tir_id"]
#         return {"user_id": user_id, "tir_id": tir_id}


class ReviewsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = Reviewsserializer

    @swagger_auto_schema(
        tags=['Tires'],
        operation_description="Этот ендпоинт предоставляет "
                              "возможность оставить отзыв,"
                              "так же оценить товар по рейтингу",
        )
    def post(self, request, *args, **kwargs):
        serializer = Reviewsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Reviews.objects.filter(id=self.kwargs["pk"])
        else:
            return Reviews.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#
# @api_view(['GET', 'POST'])
# def addcartview(request):
#
#
#     return Response({'mesic':'hello'})

class TiresRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tires.objects.all()
    serializer_class = TiresidSerializer

    @swagger_auto_schema(
        tags=['Tires'],
        operation_description="Этот ендпоинт предоставляет "
                              "возможность редактировать "
                              "текущий товар. ",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return Tires.objects.filter(id=self.kwargs["pk"])


class FavoriteAPIView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()


class RemoveFromFavoritesView(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=['Favorite'],
        operation_description="Этот ендпоинт предоставляет "
                              "возможность редактировать "
                              "текущий товар в избранном. ",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return Favorite.objects.filter(id=self.kwargs["pk"])

    # @swagger_auto_schema(
    #     tags=['Favorite'],
    #     manual_parameters=[
    #         openapi.Parameter('tir_id', openapi.IN_PATH,
    #                           description="ID шины, которую вы хотите удалить из избранного",
    #                           type=openapi.TYPE_INTEGER),
    #     ],
    #     responses={
    #         204: "Tires removed from favorites successfully.",
    #     }
    # )
    # def delete(self, request, *args, **kwargs):
    #     try:
    #         user = request.user
    #         tir_id = self.kwargs.get('tir_id')
    #
    #         if not tir_id:
    #             return Response({
    #                 'error': 'fav_id parameter is missing.'},
    #                 status=status.HTTP_400_BAD_REQUEST)
    #
    #         book = get_object_or_404(Tires, id=tir_id)
    #
    #         try:
    #             favorite_tires = Favorite.objects.get(user=user, tires=tires)
    #             favorite_tires.delete()
    #             return Response(status=status.HTTP_204_NO_CONTENT)
    #         except Favorite.DoesNotExist:
    #             return Response({
    #                 'message': 'Tires is not in favorites.'},
    #                 status=status.HTTP_404_NOT_FOUND)
    #     except Exception as e:
    #         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

