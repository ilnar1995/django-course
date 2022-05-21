#from unicodedata import category
#from unicodedata import category
import email
from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from .forms import *
from django.urls import reverse                                             #если вам нужно использовать что-то похожее на тег шаблона url в вашем коде
from django.core.mail import send_mail

def index(request):
    if request.method == "POST":
        name = request.POST.get("name") # получить значение поля Имя 
        age = request.POST.get("age") # получить значение поля Возраст 
        output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1}</hЗ>".format(name, age) 
        return HttpResponse(output) 
    else: 
        userform = UserForm1() 
        return render(request, "main/index.html", {"form":userform}) 
def field1(request):
    if request.method == "POST": 
        name = request.POST.get("name") # получить значение поля Имя 
        age = request.POST.get("age") # получить значение поля Возраст 
        output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1}</hЗ>".format(name, age) 
        return HttpResponse(output) 
    else: 
        userform = UserForm1() 
        return render(request, "main/field1.html", {"form":userform})
def field2(request):
    if request.method == "POST":
        userform = UserForm2(request.POST) 
        if userform.is_valid():                                                                                 #метод is_valid(), который выполняет проверку всех полей формы на ошибку
            print(userform.cleaned_data)                                                                        #отобразит словарь cleaned_data в консоли 
            #name = userform.cleaned_data["name"] 
            #return HttpResponse("<h2>Имя введено коррректно -{0}</h2>".format (name)) 
    else:
        userform = UserForm2()
    return render(request, "main/field2.html", {"form": userform})
def field3(request):
    if request.method == "POST":
        form = UserForm3(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = [form.cleaned_data['recipient']]
            cc_myself = form.cleaned_data['cc_myself']

            sender = 'nnnooo2@yandex.ru'
            if cc_myself and (not (sender in recipient)):
                recipient.append(sender)

            send_mail(subject, message, sender, recipient)
    else:
        form = UserForm3()
    return render(request, "main/field3.html", {"form": form})
def link(request):
    data = {"age" : 80}
    cat = ["Ноутбуки", "Принтеры", "Сканеры", "диски", "Шнуры"]
    return render(request, "main/for_and_if.html", context={"data":data,"cat":cat}) 
#def link(request):
#    return HttpResponse("<h2>0 сайте</h2>")        #простой вывод информации
def contact(request):  
    header = "Адрес" # обычная переменная 
    addr = ("г. Москва", "ул. Короленко","д. 24" ) # кортеж 
    emailadress = "pochta@gmail.com"
    tell = "+7(945)345-67-21"
    data = { "header": header, "address": addr, "emailadress" : emailadress, "tell":tell}    
    return render(request, "main/contact.html", context=data)
def contact1(request):           #временная переадресация
    return HttpResponseRedirect(reverse('contact')) 
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


