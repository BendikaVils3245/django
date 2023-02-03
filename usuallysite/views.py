from django.http import HttpResponse
from django.shortcuts import render



def first_page(request):
    a = '<h1>sss</h1>'
    txt = 'txt'
    return render(request, './index.html',{
        'a': a,
        'text': txt
    })