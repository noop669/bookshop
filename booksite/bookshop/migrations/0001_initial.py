# Generated by Django 4.1.7 on 2023-03-05 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_book', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('in_stock', models.BooleanField(verbose_name='В наличие')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('date_re_published', models.DateField(verbose_name='Год издания')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['name_book'],
            },
        ),
        migrations.CreateModel(
            name='delivery_city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=60, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город доставки',
                'verbose_name_plural': 'Города доставки',
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_genre', models.CharField(db_index=True, max_length=60, verbose_name='Жанр')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['name_genre'],
            },
        ),
        migrations.CreateModel(
            name='supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('book', models.ManyToManyField(to='bookshop.book', verbose_name='Книги')),
            ],
        ),
        migrations.CreateModel(
            name='Chek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('date_create', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('delivery_on', models.BooleanField(default=False, verbose_name='Доставлен')),
                ('books', models.ManyToManyField(to='bookshop.book', verbose_name='Книги')),
                ('delivery_city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshop.delivery_city', verbose_name='Доставка в')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-date_create'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookshop.genre', verbose_name='Жанр'),
        ),
    ]