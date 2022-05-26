from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from sympy import content

from women.forms import AddPostForm

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0
    }

    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    if request.method == "POST":
        form = AddPostForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()                                             #для форм связанных с моделью
            return redirect('home')                                 #для форм связанных с моделью
            #try:                                                   #для форм не связанных с моделью
            #    Women.objects.create(**form.cleaned_data)          #для форм не связанных с моделью
            #    return redirect('home')                            #для форм не связанных с моделью
            #except:                                                #для форм не связанных с моделью
            #    form.add_error(None, 'Ошибка добавления данных')   #для форм не связанных с моделью
    else:
        form = AddPostForm()    
    return render(request, 'women/addpage.html', {'form':form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_slug):
    post =get_object_or_404(Women, slug=post_slug)         # функция вибирает из модели Women пост с первичным ключом post_id, если не находит то выдает ошибкиу 404

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context=context)

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_id
    }

    return render(request, 'women/index.html', context=context)