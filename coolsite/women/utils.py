# создали сами для устранения дублировании в views.py

from unicodedata import category
from matplotlib.pyplot import cla
from django.db.models import Count

import women
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]

class DataMixin:
    def get_user_context(self, **kwargs):                       #функция для формирования и динамического и статического контекста
        context = kwargs   
        cats = Category.objects.annotate(Count('women'))        #получаем категории и добавляем атрибут с колич-ом постов связанных с этой рубрикой

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:              #проверка авторизации пользователья
            user_menu.pop(1)                                    #удаляем ссылку длбавления статьи для неавторизованных пользователей


        context['menu'] = user_menu                                  #добавляем пункты 
        context['cats'] = cats
        if 'cat_selected' not in context: 
            context['cat_selected'] = 0
        return context