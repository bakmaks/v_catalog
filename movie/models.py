from django.db import models
from django.utils.text import slugify
import time

from .utils import code_str


# Абстрактная модель для создания моделей Фильмов и сериалов
class AbstractVideo(models.Model):
    ru_title = models.CharField(max_length=200, verbose_name='Название', blank=False)
    en_title = models.CharField(max_length=200, verbose_name='Оригинальное Название')
    product_year = models.PositiveSmallIntegerField(verbose_name='Год', default=2020)
    slug = models.SlugField(max_length=100, unique=True)
    country = models.CharField(verbose_name='Старна', max_length=50)
    description = models.TextField(verbose_name='Описание', max_length=1000)
    poster = models.ImageField(upload_to='images/%Y/%m/%d/')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.ru_title} {self.product_year}'

    def save(self, *args, **kwargs):
        # Создаёт уникальный слаг
        self.slug = slugify(code_str(self.ru_title) + str(time.time()))
        super().save(*args, **kwargs)


# Модель  фильмов
class Film(AbstractVideo):
    class Meta:
        ordering = ['ru_title']


# Модель сериалов
class TVSeries(AbstractVideo):
    number_of_episodes = models.PositiveSmallIntegerField(verbose_name='Кол-во серий')
    season_number = models.PositiveSmallIntegerField(verbose_name='Номер сезона')

    def __str__(self):
        return f'{super().__str__()} сезон {self.season_number}'
