from goods_model.models import GoodsMod,CategoryMod,PhotoGoods
from rest_framework import serializers


class PhotoGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGoods
        fields = '__all__'  # 'photo' добавлено для отображения изображения



class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsMod
        fields = '__all__'


class CategoryRest(serializers.ModelSerializer):
    class Meta:
        model = CategoryMod
        fields = '__all__'