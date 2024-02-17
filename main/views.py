from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED,HTTP_500_INTERNAL_SERVER_ERROR
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


@api_view(['GET'])
def get_contact_view(request):
    queryset = Contact.objects.last()
    serializers = ContactSerializer(queryset, many=False)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['POST'])
def create_contact_view(request):
    try:
        name = request.data.get('name')
        email = request.data.get('email')
        number = request.data.get('number')
        contact = ContactUs.objects.create(name=name, email=email, number=number)
        data = {
            'success': True,
            'message': ContactUsSerializer(contact).data
        }
        status = HTTP_201_CREATED
    except Exception as e:
        data = {
            'success': False,
            'error': f'{e}'
        }
        status = HTTP_500_INTERNAL_SERVER_ERROR
    return Response(data, status)


@api_view(['GET'])
def get_contact_networks_view(request):
    queryset = Footer.objects.last()
    serializers = FooterSerializer(queryset, many=False)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_design_apartment_view(request):
    queryset = DesignApartment.objects.all().order_by('-id')[:4]
    serializers = DesignApartmentSerializer(queryset, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_info_apartment_view(request):
    queryset = Info.objects.last()
    serializers = InfoSerializer(queryset, many=False)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_good_realtors_view(request):
    queryset = GoodRealtor.object.all().order_by('-id')[:4]
    serializers = GoodRealtorSerializer(queryset, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_useful_realtors_view(request):
    queryset = UsefulRealtor.objects.all().order_by('-id')[:3]
    serializers = UsefulRealtorSerializer(queryset, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_work_view(request):
    queryset = Work.objects.all().order_by('-id')[:3]
    serializers = WorkSerializer(queryset, many=True)
    return Response(serializers.data, status=HTTP_200_OK)


@api_view(['GET'])
def get_realtor_view(request):
    queryset = Realtor.objects.all().order_by('-rating')
    comment_count = Comment.objects.filter(comment=request.user).count()
    serializers = {
        'queryset': RealtorSerializer(queryset, many=True).data,
        'comment_count': comment_count
    }
    return Response(serializers, status=HTTP_200_OK)

