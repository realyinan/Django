from django.urls import path, re_path
from App.views import *

urlpatterns = [
    # 首页
    path('index/', index, name='index'),

    # 用户列表
    path('userlist/', user_list, name='userlist'),

    # 用户详情
    # 单个参数
    path('userdetail/<int:uid>/', user_detail, name='userdetail'),

    # 多个参数
    path('userab/<int:a>/<int:b>/', user_ab_view, name='userab'),
    # <int: a> 整数
    # <str: a> 字符型
    path('userba/<int:a>/<int:b>/', user_ba_view, name='userba'),
    # 正则的写法
    # re_path(r'userba/(?P<a>\d+)/(?P<b>\d+)/', user_ba_view, name='userba')

    # 重定向
    path('myredirect/', my_redirect),

]