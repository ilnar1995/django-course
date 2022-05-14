from cProfile import label
from unicodedata import name
from django import forms 


class UserForm(forms.Form):
    name = forms.CharField(label= "Имя клиента", required=False,  initial=' Ваше имя', help_text='He более 100 символов')
    age = forms.IntegerField(label= "Возраст клиента")
    captcha_answer = forms.IntegerField(label='2 + 2', label_suffix=' =') 
    name1 = forms.CharField(label= "Ввод пароля", widget=forms.PasswordInput) 
    name2 = forms.CharField(label= "Ввод файла", widget=forms.FileInput) 
    asdf = forms.FileField(label= "Возврат файла")

class CoппnentForm ( forms. Form) :
    name = forms. CharField( initial=' Ваше имя' ) 
    url = forms.URLField(initial='http://') 
    coппnent = forms. CharField() 
f = CoппnentForm(auto_id=False) 
    