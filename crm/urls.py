"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from apps.web.views import order
from apps.api.views import account

urlpatterns = [


    # 路由分发
    path('api/', include("apps.api.urls", namespace='x1')),
    path('web/', include("apps.web.urls", namespace='x2')),

    path('mypath_info/', account.mypath_info),



    # """
    # 纯粹帮助提取功能的URL，防止重复编写。
    # 手动路由分发，可以与app无关。
    # 类似路由分发 include()
    # """
    path('user/', ([
                   path('add/', account.login),
                   path('delete/', account.login),   # /user/delete/
                   path('edit/', account.login),
                   path('list/', account.login),
               ], None, None)),


    # 简单的路由
    # # path('admin/', admin.site.urls),
    # path('home/', views.home),
    # path('news/<int:num>/edit/', views.news),  # 也可以加 "？"
    # path('article/', views.article),  # 后面加 "？"
    # # re_path(r'users/(\w+-\d+)', views.users_id),
    # # re_path(r'users/(\w+-\d+)/(\d+)/', views.users_param),
    # re_path(r'users/(?P<uid>\w+-\d+)/(?P<age>\d+)/', views.users_param),
]
