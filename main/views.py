from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.


@api_view(['GET'])
def get_banner_view(request):
    queryset = Banner.objects.last()
    serializer = BannerSerializer(queryset, many=False)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_apartments_view(request):
    queryset = Apartment.objects.all().order_by('-id')[:6]
    serializers = ApartmentSerializer(queryset, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_type_purchase_view(request):
    queryset = TypePurchase.objects.all().order_by('-id')[:3]
    serializers = TypePurchaseSerializer(queryset, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_apartment_view(request):
    queryset = Apartment.objects.all().order_by('-id')[:6]
    serializers = ApartmentSerializer(queryset, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_banner_discount_view(request):
    queryset = BannerDiscount.objects.last()
    serializers = BannerDiscountSerializer(queryset, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_apartment_single_view(request, pk):
    queryset = Apartment.objects.get(id=pk)
    queryset.view += 1
    queryset.save()
    serializers = ApartmentSerializer(queryset, many=False)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_popular_apartment_view(request):
    queryset = Apartment.objects.all().order_by('-view')[:4]
    serializers = ApartmentSerializer(queryset, many=True)
    return Response(serializers.data, status=HTTP_200_OK)








