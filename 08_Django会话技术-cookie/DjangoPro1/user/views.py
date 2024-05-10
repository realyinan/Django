import datetime

from django.shortcuts import render, HttpResponse, redirect, reverse
from user.models import *
def index(request):
    # cookie
    userid = request.COOKIES.get('userid', 0)

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

            # 3. 设置cookies
            #   注意: a. cookie存储在浏览器本地
            #        b. cookie不能跨域, 不能为中文
            #        c. cookie存储的内容是字符串, 不能为中文, 一般存储大小不要超过4kb
            #        d. cookie由后端创建, 返回给前端保存
            response = redirect(reverse('index'))
            # response.set_cookie('userid', user.id, max_age=7*24*3600)  # max_age: 秒
            # response.set_cookie('userid', user.id, expires=datetime.datetime(2025, 1, 2, 3, 4, 5))  # expire: 过期日期
            response.set_cookie('userid', user.id,
                                expires=datetime.datetime.now() + datetime.timedelta(days=10))  # 10天后过期

            # 3. 跳转到其他页面
            return response

# 注销
def logout(request):
    response = redirect(reverse('index'))
    # 删除cookie: 注销
    response.delete_cookie('userid')
    return response

























