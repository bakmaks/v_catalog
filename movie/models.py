from django.core import validators
from django.db import models
from django.utils.text import slugify
import time
import logging

from .utils import code_str

logger = logging.getLogger(__name__)


# ----------Абстрактная модель для создания моделей Фильмов и сериалов-----------------------------------------
class AbstractVideo(models.Model):
    ru_title = models.CharField(max_length=200, verbose_name='Название', blank=False)
    title = models.CharField(max_length=200, verbose_name='Оригинальное Название', default='----------', blank=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    country = models.CharField(verbose_name='Старна', blank=True, max_length=50)
    description = models.TextField(verbose_name='Описание', blank=True, max_length=1000)
    poster = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    categories = models.ManyToManyField('Category', blank=True, verbose_name='список жанров')
    verified = models.BooleanField(verbose_name='Проверено', default=False)
    IMDB_rating = models.DecimalField(verbose_name='IMDB', blank=True, default=0.0, max_digits=2, decimal_places=1,
                                      validators=[validators.MaxValueValidator(9.9),
                                                  validators.MinValueValidator(0.0)])
    KPoisk_rating = models.DecimalField(verbose_name='Кинопоиск', default=0.0, blank=True, max_digits=2,
                                        decimal_places=1, validators=[validators.MaxValueValidator(9.9),
                                                                      validators.MinValueValidator(0.0)])
    product_year = models.PositiveSmallIntegerField(verbose_name='Год', default=2020,
                                                    validators=[validators.MinValueValidator(1900),
                                                                validators.MaxValueValidator(2100)])

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.ru_title} / {self.product_year}'

    def save(self, *args, **kwargs):
        # Создаёт уникальный слаг
        self.slug = slugify(code_str(self.ru_title) + str(time.time()))
        super().save(*args, **kwargs)


# ----------------------Категории------------------------------------------------
class Category(models.Model):
    title = models.CharField(verbose_name='Жанр', max_length=50)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Создаёт уникальный слаг
        self.slug = slugify(code_str(self.title) + str(time.time()))
        super().save(*args, **kwargs)


# ----------------------Модель  фильмов-----------------------------------------------
class Film(AbstractVideo):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['ru_title']


# ----------------------Модель сериалов------------------------------------------------
class TVSeries(AbstractVideo):
    number_of_episodes = models.PositiveSmallIntegerField(verbose_name='Кол-во серий')
    season_number = models.PositiveSmallIntegerField(verbose_name='Номер сезона')

    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'
        ordering = ['ru_title']

    def __str__(self):
        return f'{super().__str__()} / сезон {self.season_number}'