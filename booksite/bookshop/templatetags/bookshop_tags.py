from django import template
from bookshop.models import *

register = template.Library()

@register.simple_tag()
def get_genres():
    return Genre.objects.all()

@register.inclusion_tag('bookshop/list_genre.html')
def show_genre(sort=None, genre_selected=0):
    if not sort:
        genres = Genre.objects.all()
    else:
        genres = Genre.objects.order_by(sort)
    return {"genres": genres, 'genre_selected': genre_selected}

@register.inclusion_tag('bookshop/main_menu.html')
def show_menu():
    menu = [{'title': "Поддержка", 'url_name': 'contact'},
            {'title': "Корзина", 'url_name': 'cart'}]
    return {'menu': menu}
