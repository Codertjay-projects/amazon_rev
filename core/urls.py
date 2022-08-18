from django.contrib import admin
from django.urls import path

from core.views import ProductListAPIView, CategoryListView

urlpatterns = [
    path("", CategoryListView.as_view(), name="category_list"),
    path("products/<str:category__name>/", ProductListAPIView.as_view(), name="product_list"),
]
