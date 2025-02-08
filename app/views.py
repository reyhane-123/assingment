from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

list1=[
    {"id":1,"name":"class_python"},
    {"id":2,"name":"class_html"},
    {"id":3,"name":"class_jango"},
    {"id":4,"name":"class_c#"}
]

def detail (request,id):
    select={}
    for item in list1:
        if item['id'] == 2:
            select==item
            return render(request,'detail/dore.html', context=select)
        else:
            return render(request,'detail/404.html', context=select)