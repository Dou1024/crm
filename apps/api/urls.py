from django.urls import path, re_path
from apps.api.views import account
from django.conf.urls import url    # 不光引入了系统的，还引入了当前环境里的url
urlpatterns = [
    path('main1/', account.main1, name='main1'),
    # path('auth/<str:role>/', account.auth, name='v1'),
    # re_path(r'jump1/(\d+)/', account.jump1, name='jump1'),
    # re_path(r'login/(\d+)/(\w+)/', account.login, name='v2'),
    # re_path(r'login/(?P<num>\d+)/(?P<str1>\w+)/', account.login, name='v4'),
    re_path(r'home/', account.home, name='home'),      # 与web里的相同，这里用namespace区分的
    # url('^index/$', account.index, name='index')
]
app_name = "api"
