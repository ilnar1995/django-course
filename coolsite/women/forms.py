from unicodedata import category
from django import forms
from .models import *

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



#class AddPostForm(forms.Form):                                                     #для форм не связанных с моделью
#    title = forms.CharField(max_length=255)
#    slug = forms.SlugField(max_length=255)
#    content = forms.CharField(widget=forms.Textarea(attrs={'cols':68, 'rows':10}))
#    is_published = forms.BooleanField()
#    cat = forms.ModelChoiceField(queryset=Category.objects.all())

