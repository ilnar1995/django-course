import email
from unicodedata import category
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class AddPostForm(forms.ModelForm):                                                 #для форм связанных с моделью
    def __init__(self, *args, **kwargs):                                            #функция чтобы поменять начальное значение поля 'cat'
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:                                                                     #class для вывода формы 'cat'
        model = Women                                                               #связывает форму с моделью Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']       #список полей котор надо отобразить в форме
        widgets={                                                                   #атрибут чтоб менять стили полей
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':60, 'rows':10}),
        }

    def clean_title(self):                                                          #метод для создания валидатора для длины title
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise forms.ValidationError('Длина превышает 200 символов')

        return title

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))            #переопределили стандартные атрибуты базового класса для изменения свойтва
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'})) 
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))          #переопределили стандартные атрибуты базового класса для изменения свойтва
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))   #переопределили стандартные атрибуты базового класса для изменения свойтва
    class Meta:                                                                     #class для расширения базового класса
        model = User                                                                #модель юзер это модель котор работает с таблицей auth_user
        fields = ('username', 'password1', 'password2', 'email')                    #список полей котор надо отобразить в форме(если не вносить какой либо атрибут, данные не вносились в БД)
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))



#class AddPostForm(forms.Form):                                                     #для форм не связанных с моделью
#    title = forms.CharField(max_length=255)
#    slug = forms.SlugField(max_length=255)
#    content = forms.CharField(widget=forms.Textarea(attrs={'cols':68, 'rows':10}))
#    is_published = forms.BooleanField()
#    cat = forms.ModelChoiceField(queryset=Category.objects.all())

