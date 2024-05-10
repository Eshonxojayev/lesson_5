from django.urls import path
from .views import CountryAPIView, CityAPIView, AddressAPIView, CustomersAPIView
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import LandingPageView, UsersLogoutView, UsersLoginView, UserRegisterView, ContactView, ProfileView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Customer API",
        description="Customer Application demo",
        default_version="v1",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='pipsudo@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)
router = DefaultRouter()
router.register('customers', CustomersAPIView)
router.register('addresses', AddressAPIView)
router.register('city', CityAPIView)
router.register('country', CountryAPIView)

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('logout/', UsersLogoutView.as_view(), name='logout'),
    path('login/', UsersLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
    path('', include(router.urls)),
    path('country/', CountryAPIView.as_view({'get': 'list'}), name='country'),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)