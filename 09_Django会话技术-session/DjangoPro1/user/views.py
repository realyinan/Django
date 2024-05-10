import datetime

from django.shortcuts import render, HttpResponse, redirect, reverse
from user.models import *
def index(request):
    # session
    userid = request.session.get('userid', 0)

    # 获取登录的用户
    user = UserModel.objects.filter(id=userid).first()

    return render(request, 'index.html', {'user': user})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        # 接受前端提交过来的数据
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        age = request.POST.get('age')
        print(uname, passwd, age, sep='-----')

        # 先判断用户是否已经注册过
        users = UserModel.objects.filter(username=uname)
        if users.exists():
            return HttpResponse('用户名已经存在')
        # 实现注册功能
        try:
            user = UserModel()
            user.username = uname
            user.password = passwd
            user.age = age
            user.save()
        except Exception as e:
            return HttpResponse('注册失败')
        # 注册成功后跳转到登录页面
        return redirect(reverse('login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # 登录功能
        # 1. 先接受前端提交过来额数据
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        # 2. 登录验证
        users = UserModel.objects.filter(username=uname, password=passwd)
        if users.exists():
            # 获取当登录的用户对象
            user = users.first()

            response = redirect(reverse('index'))

            # 3. 设置session
            request.session['userid'] = user.id
            request.session.set_expiry(7*24*3600)

            # 3. 跳转到其他页面
            return response

# 注销
def logout(request):
    response = redirect(reverse('index'))
    # 删除session
    session_key = request.session.session_key
    request.session.delete(session_key)
    return response

























