from django.shortcuts import render
from django.http import HttpResponse
from user.models import *
# 视图函数Views
def index(request):
    # 渲染模板render
    return render(request, 'index.html')

def index2(request):
    # 返回相应的response
    return HttpResponse('Index2')


def get_users(request):
    """获取所有的用户"""
    users = UserModel.objects.all()
    return render(request, 'users.html', {"users": users})

