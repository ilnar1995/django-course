#from unicodedata import category
#from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound

def index(request):
        header = "Персональные данные" # обычная переменная 
        langs = ["Английский", "Немецкий", "Испанский"] # массив 
        user = {"name": "Максим,", "age": 30} # словарь 
        addr = ("Виноградная", 23, 45) # кортеж 
        data = { "header": header, "langs": langs, "user": user, "address": addr}
        return render(request, "main/index.html", context=data) 
def link(request):
    data = {"age" : 50}
    cat = ["Ноутбуки", "Принтеры", "Сканеры", "диски", "Шнуры"]
    return render(request, "main/for_and_if.html", context={"data":data,"cat":cat}) 
#def link(request):
#    return HttpResponse("<h2>0 сайте</h2>")        #простой вывод информации
def contact(request):         
    return render(request, "main/contact.html")
def contact1(request):           #временная переадресация
    return HttpResponseRedirect("/contact") 
def products(request1, productid=1): 
    category=request1.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1} </h2>".format(productid,category) 
    return HttpResponse(output) 
def users(request): 
    id = request.GET.get("id", 1) 
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя:{1}</hЗ>".format(id,name) 
    return HttpResponse(output)
def details(request):           #постоянная переадресация
    return HttpResponsePermanentRedirect("/")
def date(request):           #постоянная переадресация
    return render(request, "main/date.html")


def m404(request): 
    return HttpResponseNotFound("<h2>Not Found</h2>")