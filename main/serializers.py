from rest_framework import serializers
from .models import *


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Banner
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Apartment
        fields = '__all__'


class TypePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = TypePurchase
        fields = '__all__'


class BannerDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = BannerDiscount
        fields = '__all__'
