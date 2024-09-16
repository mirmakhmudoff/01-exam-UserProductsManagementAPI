from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
