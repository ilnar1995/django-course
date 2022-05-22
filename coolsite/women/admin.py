from django.contrib import admin

from .models import *
# Register your models here.

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')          #те поля гду нужны ссылки на редактирование
    list_display_links =('id', 'title')                                             #те поля гду нужны ссылки на редактирование
    search_fields = ('title', 'content')                                            #где можно производить поиск

admin.site.register(Women, WomenAdmin)                                              # для регистрации модели в админ панели (второй параметр для редактирования панели)
admin.site.register(Category)

