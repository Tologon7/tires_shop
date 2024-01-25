from django.urls import path
from .views import (
    Tiresviewid,
    Tiresview,
    Categoryviewid,
    Categoryview,
    ReviewsView,






)

urlpatterns = [

    path('category/<int:cat_id>/', Categoryviewid.as_view()),
    path('category/', Categoryview.as_view()),
    path('list/<int:tir_id>/', Tiresviewid.as_view()),
    path('list/', Tiresview.as_view()),
    path('reviews/<int:rev_id>/', ReviewsView.as_view()),






]