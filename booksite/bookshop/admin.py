from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_book', 'author', 'date_re_published', 'get_html_photo', 'in_stock', 'price', 'genre')
    list_display_links = ('id', 'name_book')
    search_fields = ('name_book', 'author')
    list_filter = ('author', 'genre')
    prepopulated_fields = {'slug': ('name_book',)}
    fields = ('name_book', 'slug', 'author', 'date_re_published', 'photo', 'get_html_photo', 'in_stock', 'price', 'genre', 'description')
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')

    get_html_photo.short_description = "Фото"


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_genre')
    list_display_links = ('id', 'name_genre')
    search_fields = ('name_genre',)
    prepopulated_fields = {'slug': ('name_genre',)}


class SupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'price')
    list_display_links = ('id',)
    search_fields = ('id',)


class ChekAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'date_create', 'delivery_city', 'delivery_on')
    list_display_links = ('id',)
    search_fields = ('id', 'date_create')
    list_filter = ('id', 'date_create')


class Delivery_cityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')
    list_display_links = ('city',)
    search_fields = ('city',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'author', 'created_date')
    list_display_links = ('book', 'author')
    search_fields = ('created_date', 'author')


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Chek, ChekAdmin)
admin.site.register(supply, SupplyAdmin)
admin.site.register(delivery_city, Delivery_cityAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.site_title = 'Админ-панель Bookshop'
admin.site.site_header = 'Админ-панель Bookshop'
