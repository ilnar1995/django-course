from re import template
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from matplotlib.style import context
from sympy import content

from women.forms import AddPostForm

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'                  #переопределение шаблона (по умолчанию он ищет "women/women_list.html")
    context_object_name = 'posts'                       #переопределяем имя переменной класса представления WomenHome (стандартное "object_list")
    #extra_context = {'title':'Главная страница'}

    def get_context_data(self, object_list=None, **kwargs):     #функция для формирования и динамического и статического контекста
        context = super().get_context_data(**kwargs)            #через базовый класс ListView получам уже существующий контекст
        context['menu'] = menu                                  #добавляем пункты 
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):                                     #функ для фильтрации по модели Women
        return Women.objects.filter(is_published=True)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')                          #если надо после заполнения форма перейти на какой либо URL а не по get_absolute_url()

    def get_context_data(self, object_list=None, **kwargs):     #функция для формирования и динамического и статического контекста
        context = super().get_context_data(**kwargs)            #через базовый класс ListView получам уже существующий контекст
        context['menu'] = menu                                  #добавляем пункты 
        context['title'] = 'Добавление статьи'
        context['cat_selected'] = 0
        return context



def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'                                #переопределение перемнной (по умолчанию "slug")
    context_object_name = 'post' 

    def get_context_data(self, object_list=None, **kwargs):     #функция для формирования и динамического и статического контекста
        context = super().get_context_data(**kwargs)            #через базовый класс ListView получам уже существующий контекст
        context['menu'] = menu                                  #добавляем пункты 
        context['title'] = str(context['post'].title)
        context['cat_selected'] = context['post'].cat_id
        return context




def delete_post(request, post_slug):
    Women.objects.filter(slug=post_slug).delete()  
    return redirect('home')


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'                  #переопределение шаблона (по умолчанию он ищет "women/women_list.html")
    context_object_name = 'posts'                       #переопределяем имя переменной класса представления WomenHome (стандартное "object_list")
    allow_empty = False                                 #атрибут выдает ошмбук 404 если страница не найдена
    #extra_context = {'title':'Главная страница'}

    def get_context_data(self, object_list=None, **kwargs):     #функция для формирования и динамического и статического контекста
        context = super().get_context_data(**kwargs)            #через базовый класс ListView получам уже существующий контекст
        context['menu'] = menu                                  #добавляем пункты 
        context['title'] = 'Категория: '+ str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):                                     #функ для фильтрации по модели Women
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'],is_published=True)






        #для оборбажения через функции представления

#def index(request):
#    posts = Women.objects.all()
#    context = {
#        'posts': posts,
#        'menu': menu,
#        'title': 'Главная страница',
#        'cat_selected': 0
#    }
#    return render(request, 'women/index.html', context=context)


#def addpage(request):
#    if request.method == "POST":
#        form = AddPostForm(request.POST,request.FILES)
#        if form.is_valid(): 
#            form.save()                                             #для форм связанных с моделью
#            return redirect('home')                                 #для форм связанных с моделью
#            #try:                                                   #для форм не связанных с моделью
#            #    Women.objects.create(**form.cleaned_data)          #для форм не связанных с моделью
#            #    return redirect('home')                            #для форм не связанных с моделью
#            #except:                                                #для форм не связанных с моделью
#            #    form.add_error(None, 'Ошибка добавления данных')   #для форм не связанных с моделью
#    else:
#        form = AddPostForm()    
#    return render(request, 'women/addpage.html', {'form':form, 'menu': menu, 'title': 'Добавление статьи'})
 


#def show_post(request, post_slug):
#    post =get_object_or_404(Women, slug=post_slug)         # функция вибирает из модели Women пост с первичным ключом post_id, если не находит то выдает ошибкиу 404
#
#    context = {
#        'post': post,
#        'menu': menu,
#        'title': post.title,
#        'cat_selected': post.cat_id,
#    }
#    return render(request, 'women/post.html', context=context)

#def show_category(request, cat_slug):
#    posts = Women.objects.filter(cat__slug=cat_slug)
#    for item in posts:
#        pass
#    print("item.cat_id")
#    context = {
#        'posts': posts,
#        'menu': menu,
#        'title': 'Главная страница',
#        'cat_selected': cat_slug
#    }
#    return render(request, 'women/index.html', context=context)