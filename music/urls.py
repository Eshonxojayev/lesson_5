from django.urls import path, include
from .views import ArtistAPIView, SongSetAPIView, AlbomAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('songs', SongSetAPIView)
router.register('albom', AlbomAPIViewSet)
urlpatterns = [
    path('artist/', ArtistAPIView.as_view({'get': 'list'}), name='artist-list'),
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]
