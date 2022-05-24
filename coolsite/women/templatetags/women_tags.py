from atexit import register
from django import template
from women.models import *

register = template.Library() #создаем экземпляр класса library через котор происходит регистрация собственных шаблонных тэгов

@register.simple_tag(name='getcats')          # декотратор для превращения функции в тэг
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('women/list_categories.html')   # тэг который возр-ет шаблон list_categories.html с передачей в нее параметров "cats"
def show_categories(sort=None, selected=None):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    
    return {"cats":cats, "cat_selected":selected}