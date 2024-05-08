from django.urls import path, include
from .views import BillingAPIView, CustomerViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('customerset', CustomerViewSet, basename='customerset')
router.register('product', ProductViewSet, basename='product')
router.register('billing', BillingAPIView, basename='billing')

urlpatterns = [
    path('', include(router.urls)),
    path('billing', BillingAPIView.as_view({'get': 'list'}), name='billing'),
    path('api-auth/', include('rest_framework.urls')),
]