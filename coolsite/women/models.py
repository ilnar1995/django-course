from django.db import models
from django.urls import reverse
from sqlalchemy import ForeignKey

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name = "заголовок")            # verbose_name исп-ся для измнения поля в шапке админ панели
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")  # unique=True означает уникальность, db_index чтобы это поле было индесируемым для быстрого поиска
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name = "фото")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)        # Category в кавычках потому что он идет ниже (если был бы высше можно было бы без кавычек) null=True т.к. в таблице caregory еще нет значении

    def __str__(self):
        return self.title                                           # чтобы возвращать заголовок текущей записи

    def get_absolute_url(self):                                     # стандартная админ панель использует именно такое название метода класса (дать именно такое название)
        return reverse('post', kwargs={'post_slug': self.slug})         # формирование динамич url адреса связанный с базой даннх ('post_id' это парамтр получаемый из URL)

    class Meta:
        verbose_name = "Известные женщины"                          # чтобы на админ панели названия были как мы хотим
        verbose_name_plural = "Известные женщины"                   # чтобы на админ панели названия были как мы хотим
        ordering = ['-time_create', 'title']                        # для сортировки(сначала по полю 'time_create' если одинаково то по 'title')

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Имя кат.')   # verbose_name исп-ся для измнения поля в шапке админ панели
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL") 

    def __str__(self):
        return self.name                                            # чтобы возвращать имя категории

    def get_absolute_url(self):                                     
        return reverse('category', args=[self.pk])      # в видео было kwargs={'cat_id': self.pk}
        
    class Meta:
        verbose_name = "Категории"                          # чтобы на админ панели названия были как мы хотим
        verbose_name_plural = "Категории"                   # чтобы на админ панели названия были как мы хотим
        ordering = ['name']                        # для сортировки(сначала по полю 'time_create' если одинаково то по 'title')