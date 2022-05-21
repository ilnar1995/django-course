from cProfile import label
from unicodedata import name
from django import forms 


class UserForm1(forms.Form):
    name = forms.CharField(label= "Имя клиента", required=False,  initial=' Ваше имя', help_text='He более 100 символов')
    age = forms.IntegerField(label= "Возраст клиента")
    captcha_answer = forms.IntegerField(label='2 + 2', label_suffix=' =') 
    name1 = forms.CharField(label= "Ввод пароля", widget=forms.PasswordInput) 
    name2 = forms.CharField(label= "Ввод файла", widget=forms.FileInput) 
    asdf = forms.FileField(label= "Возврат файла")
    file_path = forms.FilePathField(label="Bыбepитe файл", path="F:/", allow_files="True", allow_folders="True") 
    basket = forms.BooleanField(label="Пoлoжить товар в корзину")
    ling = forms.ChoiceField(label="Bыбepитe язык", choices=((1, "Английский"), (2, "Немецкий"), (3, "Французский")))
    city = forms.TypedChoiceField(label="Bыбepитe город", empty_value=None, choices=( (1, "Москва"), (2, "Воронеж"), (3, "Курск")))
    country = forms.MultipleChoiceField(label="Bыбepитe страны", choices= ( ( 1, "Англия"), (2, "Германия"), (3, "Испания"), (4, "Россия"))) 
    city = forms.TypedMultipleChoiceField(label="Bыбepитe город", empty_value=None, choices= ( ( 1, "Москва") , (2, "Воронеж"), (3, "Курск"), (4, "Томск")))
    comment = forms. CharField ( label="Комментарий", widget=forms.Textarea) 

class UserForm2(forms.Form):
    name = forms.CharField(label="Имя клиента", required=False) 
    age = forms.IntegerField(label="Boзpacт клиента", required=False) 

class UserForm3(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recipient = forms.EmailField()
    cc_myself = forms.BooleanField(label="Копию себе", required=False)

class CoппnentForm ( forms. Form) :
    name = forms. CharField(initial=' Ваше имя' ) 
    url = forms.URLField(initial='http://') 
    coппnent = forms.CharField() 

f = CoппnentForm(auto_id=False) 
    