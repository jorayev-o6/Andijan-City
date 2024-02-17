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


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Contact
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = ContactUs
        fields = '__all__'


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Footer
        fields = '__all__'


class DesignApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = DesignApartment
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Info
        fields = '__all__'


class GoodRealtorSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = GoodRealtor
        fields = '__all__'


class UsefulRealtorSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = UsefulRealtor
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Work
        fields = '__all__'


class UserRealtorSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = User
        fields = '__all__'


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Realtor
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Comment
        fields = '__all__'
