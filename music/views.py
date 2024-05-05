from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer, AlbomSerializer, SongsSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


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
    permission_classes = (IsAuthenticated,)
