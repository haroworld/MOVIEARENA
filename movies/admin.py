from django.contrib import admin
from .models import Categories, movie

# Register your models here.
admin.site.register(movie)
admin.site.register(Categories)