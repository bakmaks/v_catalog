from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Film, TVSeries, Category


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('get_poster', 'ru_title', 'title', 'product_year', 'country', 'IMDB_rating', 'KPoisk_rating',
                    'verified')
    list_display_links = ('ru_title', 'title')
    search_fields = ('ru_title', 'title', 'product_year', 'IMDB_rating', 'KPoisk_rating',)
    list_filter = ('product_year', 'country', 'IMDB_rating', 'KPoisk_rating', 'verified')

    def get_poster(self, obj):
        if obj.poster:
            return mark_safe(f'<img src="{obj.poster.url}" height="40">')
        return '---'

    get_poster.short_description = 'Постер'


@admin.register(TVSeries)
class TVSeriesAdmin(admin.ModelAdmin):
    list_display = ('get_poster', 'ru_title', 'title', 'product_year', 'country', 'IMDB_rating', 'KPoisk_rating',
                    'number_of_episodes', 'season_number', 'verified')
    list_display_links = ('ru_title', 'title')
    search_fields = ('ru_title', 'title', 'product_year', 'IMDB_rating', 'KPoisk_rating',)
    list_filter = ('product_year', 'country', 'IMDB_rating', 'KPoisk_rating', 'verified')

    def get_poster(self, obj):
        if obj.poster:
            return mark_safe(f'<img src="{obj.poster.url}" height="40">')
        return '---'

    get_poster.short_description = 'Постер'


#admin.site.register(Film, FilmAdmin)
#admin.site.register(TVSeries, TVSeriesAdmin)
admin.site.register(Category)


