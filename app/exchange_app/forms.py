from django import forms


class ExchangeForm(forms.Form):  #для форм не связанных с моделью

    slug = forms.FloatField(label='Введите число')
    fromfield = forms.ChoiceField(label='От', choices=((1, 1), (2, 2), (3, 3)))
    tofield = forms.ChoiceField(label='К')



