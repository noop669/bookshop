from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Book(models.Model):
    name_book = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    price = models.PositiveIntegerField(verbose_name='Цена')
    in_stock = models.BooleanField(verbose_name='В наличие')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    author = models.CharField(max_length=255, verbose_name='Автор')
    date_re_published = models.DateField(verbose_name='Год издания')
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, verbose_name='Жанр')

    def __str__(self):
        return self.name_book

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_slug': self.slug})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name_book']


class Genre(models.Model):
    name_genre = models.CharField(max_length=60, db_index=True, verbose_name='Жанр')
    slug = models.SlugField(max_length=60, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name_genre

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_slug': self.slug})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name_genre']


class Chek(models.Model):
    books = models.ManyToManyField('Book', verbose_name='Книги')
    count = models.PositiveIntegerField(verbose_name='Количество')
    date_create = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    delivery_city = models.ForeignKey('Delivery_city', on_delete=models.PROTECT, verbose_name='Доставка в')
    delivery_on = models.BooleanField(verbose_name='Доставлен', default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Покупатель')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date_create']


class delivery_city(models.Model):
    city = models.CharField(max_length=60, verbose_name='Город')

    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return reverse('city', kwargs={'city': self.pk})

    class Meta:
        verbose_name = 'Город доставки'
        verbose_name_plural = 'Города доставки'
        ordering = ['city']


class supply(models.Model):
    book = models.ManyToManyField('Book', verbose_name='Книги')
    count = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена')


class Comment(models.Model):
    book = models.ForeignKey('Book', on_delete=models.PROTECT, verbose_name='Книга', blank=True, null=True, related_name='comments_book')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор', blank=True, null=True)
    text = models.TextField(blank=True, verbose_name='Текст')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Коментарии'
        ordering = ['-created_date']

    def __str__(self):
        return self.pk

