from django.contrib import admin

from .models import Film, TVSeries, Category

admin.site.register(Film)
admin.site.register(TVSeries)
admin.site.register(Category)