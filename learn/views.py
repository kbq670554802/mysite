# coding:utf8
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(u"欢迎光临  自强学堂")


def home(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    return render(request, 'learn/home.html', {'string': string, 'list': list, 'dict': dict})
