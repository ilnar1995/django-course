"""taskmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from . import settings

from django.conf import settings                        # для добавления статических файлов это файл setting в этой же папке
from django.conf.urls.static import static              # для добавления статических файлов

urlpatterns = [
    path('admin/', admin.site.urls),                    # в нашем случае маршрут 'admin/' будет обрабатываться методом admin.site.urls
    path('main_project/', include('main.urls'))
] 
if settings.DEBUG: # если мы в режиме отладки то:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)   # добавления статических файлов css и тд.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
