from django.urls import path
from .views import ProductAPIView, CategoryAPIView, CommentAPIView, CartAPIView
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductListView, ProductDetailView, CartView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Product API",
        description="Product Application demo",
        default_version="v1",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='pipsudo@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)
router = DefaultRouter()
router.register('products', ProductAPIView)
router.register('categories', CategoryAPIView)
router.register('comments', CommentAPIView)
router.register('cart', CartAPIView)

urlpatterns = [
    path('shop/', ProductListView.as_view(), name='shopping'),
    path('shop/detail/<int:id>/', ProductDetailView.as_view(), name='shop-detail'),
    path('cart/<int:id>/detail', CartView.as_view(), name='cart'),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
    path('', include(router.urls)),
#    path('products/', ProductListView.as_view({'get': 'list'}), name='products'),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)