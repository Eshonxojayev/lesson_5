from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    last_updated = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

class Albom(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    cover = models.URLField()
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

class Songs(models.Model):
    title = models.CharField(max_length=100)
    cover = models.URLField(null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)