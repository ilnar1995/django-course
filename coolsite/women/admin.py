from django.contrib import admin

from .models import *
# Register your models here.

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')          #те поля которые мы хотим видить на панели админа
    list_display_links =('id', 'title')                                             #те поля где нужны ссылки на редактирование
    search_fields = ('title', 'content')                                            #где можно производить поиск
    list_editable = ('is_published',)                                               #делает редактируемым поле
    list_filter = ('is_published', 'time_create')                                   #справа добавил сайд бар для фильтрации

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')                                                   #те поля гду нужны ссылки на редактирование
    list_display_links =('id', 'name')                                              #те поля гду нужны ссылки на редактирование
    search_fields = ('name',)                                                       #где можно производить поиск


admin.site.register(Women, WomenAdmin)                                              # для регистрации модели в админ панели (второй параметр для редактирования панели)
admin.site.register(Category, CategoryAdmin)


