import requests
from django.shortcuts import render
from .forms import *

from django import forms
import json


# Create your views here.
def hello(request):
    d = requests.get('https://open.er-api.com/v6/latest/USD').json()
    r = d.get('rates')
    list1 = [(k, k) for k, v in r.items()]
    #list2 = list(r.keys())
    #list1 = [(k+1, list2[k]) for k in range(len(list2))]
    f = ExchangeForm()
    f.fields['fromfield'].choices = list1
    f.fields['tofield'].choices = list1
    result = None
    if request.method == "POST":
        #print(ExchangeForm.fromfield.widget.__dict__)
        #f.fields['fromfield'].choices = r
        #print(f.fields['fromfield'].widget.__dict__)
        #print(t.fields['fromfield'])
        #print(r)
        #print(f.fromfield.label)

        f = ExchangeForm(request.POST)
        f.fields['fromfield'].choices = list1
        f.fields['tofield'].choices = list1
        result = round(r[request.POST.get('tofield')]/r[request.POST.get('fromfield')]*float(request.POST.get('slug')),2)
        print(type(request))

    context = {'name': 'fgdf', 'r': r, 'form':f, 'result':result}
    return render(request, 'exchange_app/index.html', context)
