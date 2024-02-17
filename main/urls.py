from django.urls import path
from .views import *

urlpatterns = [
    path('get-banner/', get_banner_view, name='get-banner'),
    path('get-apartments/', get_apartments_view, name='get-apartments'),
    path('get-type-purchased/', get_type_purchase_view, name='get-type-purchased'),
    path('get-apartment/', get_apartment_view, name='get-apartments'),
    path('get-banner-discount/', get_banner_discount_view, name='get-banner-discount'),
    path('get-single-apartment/<int:pk>/', get_apartment_single_view, name='get-single-apartment'),
    path('get-popular-apartments/', get_popular_apartment_view, name='get-popular-apartments'),
    path('get-contact/', get_contact_view, name='get-contact'),
    path('create-contact/', create_contact_view, name='create-contact'),
    path('get-contact-networks/', get_contact_networks_view, name='get-contact'),
    path('get-info-apartment/', get_info_apartment_view, name='get-info-apartment'),
    path('get-good-realtors/', get_good_realtors_view, name='get-good-realtors'),
    path('get-useful-realtors/', get_useful_realtors_view, name='get-good-realtors'),
    path('get-work/', get_work_view, name='get-good-realtors'),
    path('get-realtor/', get_realtor_view, name='get-realtor'),

]
