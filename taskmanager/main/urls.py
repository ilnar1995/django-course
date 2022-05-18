from django.urls import path, re_path
from main import views
from django.views.generic import TemplateView 

urlpatterns = [
    re_path(r'^contact1/', views.contact1, name="contact1"),
    re_path(r'^contact/', views.contact, name="contact"), #    products/phones|taЬlets/
    path('link/', views.link, name="link"),                                #вариант через re_path
    path('details/', views.details),
    path('date/', views.date, name="date"),
    path('field1',views.field1, name="field1"),
    path('field2',views.field2, name="field2"),
    path('about/',TemplateView.as_view(template_name="main/about.html"), name="about"),           #ДЛЯ ПРОЯМОГО ОБРАЩЕНИЯ К ШАБЛОНУ
    #re_path(r'^products/$', views.products), # маршрут по умолчанию #вариант через re_path
    #re_path(r'^products/(?P<productid>\d+)/', views.products),      #вариант через re_path
    #re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),     #вариант через re_path
    path('products/', views.products), # маршрут по умолчанию
    path('products/<int:productid>/', views.products), 
    path('users/', views.users), # маршрут по умолчанию
    #path('users/<int:id>/<name>/', views.users),                    #передача патаметра по URL 
    path ('', views.index, name="home"),
]