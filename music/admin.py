from django.contrib import admin
from .models import Artist, Albom, Songs

admin.site.register(Artist)
admin.site.register(Albom)
admin.site.register(Songs)