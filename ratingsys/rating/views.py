# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse(u"你好!")

def home(request):
    string = u"我在学习Django"
    return render(request,'home.html',{'string':string})
