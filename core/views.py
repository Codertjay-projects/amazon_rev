# Create your views here.
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from core.models import Product, Category
from core.serializers import ProductSerializer, CategorySerializer


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    lookup_field = "category__name"
    queryset = Product.objects.all()
    search_fields = ["name", "description", "category__name"]
    filter_backends = [SearchFilter, OrderingFilter]
