from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer, AlbomSerializer, SongsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

class ArtistAPIView(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

class AlbomAPIViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

class SongSetAPIView(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('album', 'artist')
    search_fields = ['title',]
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['GET'])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        song.listened += 1
        song.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['GET'])
    def top_listened(self, request, *args, **kwargs):
        song = self.get_queryset()
        song.song.order_by('-listened')[:3]
        serializer = SongsSerializer(song, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def albom(self, request, *args, **kwargs):
        song = self.get_object()
        albom = song.albom.all()
        serializer = AlbomSerializer(albom)
        return Response(serializer.data)