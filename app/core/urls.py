from django.urls import path
from .views import CountryAPIView, ResidencyInfoAPIView

urlpatterns = [
    path('countries/', CountryAPIView.as_view(), name='display_countries'),
    path('api/country/', ResidencyInfoAPIView.as_view(), name='country-api'),
]
