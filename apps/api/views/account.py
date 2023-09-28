import json

from django.shortcuts import render, HttpResponse, redirect
import requests
from django.urls import reverse


# Create your views here.


def auth(request, role):
    name = request.GET.get("myName")
    age = request.GET.get("age")
    sex = request.GET.get("sex")

    print(name, age, sex, sep="\t\t")
    print("server feedback from fun_auth in api")
    return HttpResponse("api/auth")


def login(request):
    print("server feedback from fun_login in api")
    # 实现跳转到auth  用路径实现
    # return redirect("/api/auth/")
    res = HttpResponse("api/login")
    res["hobby"] = 123
    res.set_cookie('name', 'Jack')
    print(res)
    # 用 name 实现反向解析出 url
    # from django.urls import reverse
    # url = reverse("v1")
    # return redirect(url)

    # 当外部的地址是动态的时
    # url_v1 = reverse("v1", kwargs={"role": "abc"})
    # print(url_v1)
    # url_v2 = reverse("v2", args=(222, "ddd"))
    # print(url_v2)
    # return res
    return res
    # return HttpResponse("api/login")


def jump1(request, j1):
    # url_v2 = reverse("v2", args=(111, "ddd"))
    # print(url_v2)
    # return redirect(url_v2)
    # url1 = reverse("x1:home")  # api/home
    # url2 = reverse("x2:home")  # web/home
    # print(url1)
    # print(url2)
    return HttpResponse("success")


def home(request):
    return render(request, 'api/login.html')


def main1(request):
    # url = reverse("api:main1")
    # print(url)
    return HttpResponse("main1")


def mypath_info(request):
    # django添加的数据
    # print(request.resolver_match)   # ResolverMatch(func=apps.api.views.mypath_info, args=(), kwargs={}, url_name=None, app_names=[], namespaces=[], route=mypath_info/)

    # 1.当前的url
    # print(request.path_info)    # /mypath_info/

    # 2.url 传递的参数
    # print(request.GET)      # <QueryDict: {'name': ['dou'], 'age': ['20']}>

    # 3.请求方式  GET/POST
    # print(request.method)   # GET

    # 4.如果POST请求，传递请求题（原始数据）
    print(request.body)  # b''       # b'v1=123&v2=456'

    # 4.1 请求体+请求头       b'v1=123&v2=456'  +  content-type:application/x-www-form-urlencoded
    # 能用以下的更方便的提取出里面的数据 如：123， 456
    # 正常情况是可以拿到数据的，但是由于django csrf token机制，要去setting里注释掉

    print(request.POST)  # <QueryDict: {'v1': ['123'], 'v2': ['456']}>
    print(request.POST.get("v1"))  # 123
    print(request.POST.get("v2"))  # 456

    # 4.2 请求体+请求头   文件
    print(request.FILES)  # 文件格式           + multipart/form-data
    print(request.FILES.get("n1"))
    print(request.FILES.get("n2"))

    return HttpResponse("mypath_info")
