from django.contrib import admin

from django.utils.safestring import mark_safe
from .models import *
# Register your models here.

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_women', 'is_published')          #те поля которые мы хотим видить на панели админа
    list_display_links =('id', 'title')                                             #те поля где нужны ссылки на редактирование
    search_fields = ('title', 'content')                                            #где можно производить поиск
    list_editable = ('is_published',)                                               #делает редактируемым поле
    list_filter = ('is_published', 'time_create')                                   #справа добавил сайд бар для фильтрации
    prepopulated_fields = {"slug":("title",)}                                       #автоматический формирует слаг из title
    fields = ('title', 'slug', 'cat', 'content', 'get_html_women', 'is_published')  
    readonly_fields = ('time_create', 'time_update', 'get_html_women') 
    def get_html_women(self, object):                                               #функция чтобы показывать фото в админ панели вместо ссылок
        if object.photo:
            return  mark_safe(f"<img src='{object.photo.url}' width=50>")           #чтобы указывать не экранировать эти тэги благодаря тому что этф функ-я добавляет фильтра safe

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')                                                   #те поля гду нужны ссылки на редактирование
    list_display_links =('id', 'name')                                              #те поля гду нужны ссылки на редактирование
    search_fields = ('name',)                                                       #где можно производить поиск
    prepopulated_fields = {"slug":("name",)}                                         #автоматический формирует слаг из name


admin.site.register(Women, WomenAdmin)                                              # для регистрации модели в админ панели (второй параметр для редактирования панели)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ панель сайта n'
admin.site.site_header = 'Админ панель сайта'


