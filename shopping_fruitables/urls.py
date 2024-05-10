from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customers.views import my_custom_404_view


handler404 = 'customers.views.my_custom_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('billing.urls')),
    path('', include('customers.urls')),
    path('', include('products.urls')),
    path('api/v1/', include('music.urls')),
    path('api/v1/', include('api.urls')),
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('products.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
