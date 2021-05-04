from django.shortcuts import render
from rest_framework import generics
from shop.serializers import *
from shop.models import *


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()
