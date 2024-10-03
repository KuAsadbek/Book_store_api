from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from goods_model.models import GoodsMod,CategoryMod,PhotoGoods
from .rest_p import CategoryRest,GoodsSerializer,PhotoGoodsSerializer
from rest_framework import permissions,viewsets

class GoodsViewSet(viewsets.ModelViewSet):
    queryset = GoodsMod.objects.all()
    serializer_class = GoodsSerializer

class CategoryListCreate(viewsets.ModelViewSet):
    queryset = CategoryMod.objects.all()
    serializer_class = CategoryRest

class ProductList(viewsets.ModelViewSet):
    queryset = PhotoGoods.objects.all()
    serializer_class = PhotoGoodsSerializer

# class ProductCreate(CreateAPIView):
#     queryset = GoodsMod.objects.all()
#     serializer_class = GoodsSerializer

# class ProductUpdate(UpdateAPIView):
#     queryset = GoodsMod.objects.all()
#     serializer_class = GoodsSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class ProductDelete(DestroyAPIView):
#     queryset = GoodsMod.objects.all()
#     serializer_class = GoodsSerializer

# class ProductListCreate(ListCreateAPIView):
#     queryset = GoodsMod.objects.all()
#     serializer_class = GoodsSerializer

# class ProductCrud(RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = GoodsMod.objects.all()
#     serializer_class = GoodsSerializer

# class CategoryCrud(RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = CategoryMod.objects.all()
#     serializer_class = CategoryRest