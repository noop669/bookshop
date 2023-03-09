from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', HomeShow.as_view(), name='home'),
    path('contact/', SupportFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('re_password/', RePassword.as_view(), name='re_login'),
    path('reset_password/', ResetPassword.as_view(), name='reset_password'),
    path('logout/', logout_user, name='logout'),
    path('profile/', ShowProfile, name='profile'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('book/<slug:book_slug>/', ShowBook.as_view(), name='book'),
    path('genre/<slug:genre_slug>/', BooksGenre.as_view(), name='genre'),
    path('cart/', Order.as_view(), name='cart'),
    path('profile/my_order/', ShowProfileOrder.as_view(), name='my_order'),
    path('profile/my_comments/', ShowProfileComments.as_view(), name='my_comments'),
]
