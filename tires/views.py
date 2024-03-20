from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from tires.serializers import (
    TiresSerializer,
    Categoryserializer,
    Reviewsserializer,
    TiresidSerializer


)
from tires.models import (
    Tires,
    Category,
    Reviews,
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


class ReviewsView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = Reviewsserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        rev_id = self.kwargs.get("rev_id")
        if rev_id is not None:
            return Reviews.objects.filter(id=rev_id)
        return Reviews.objects.all()

    def get_serializer_context(self):
        user_id = self.request.user.id
        tir_id = self.kwargs.get("tir_id")
        return {"user_id": user_id, "tir_id": tir_id}


#
# @api_view(['GET', 'POST'])
# def addcartview(request):
#
#
#     return Response({'mesic':'hello'})
