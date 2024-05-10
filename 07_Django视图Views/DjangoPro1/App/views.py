from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect, reverse

# 请求
def my_request(request):
    print(request)  # <WSGIRequest: GET '/request/'>

    # request对象的属性和方法
    print(request.method)  # 请求的方法, 常见的有GET, POST
    print(request.POST)  # POST参数 <QueryDict: {}>
    print(request.GET)  # GET参数 <QueryDict: {}> 类字典对象
    print('*'*60)
    print(request.GET['name'])  # 如果name不存在, 则报错.
    print(request.GET.get('name', default='匿名用户'))  # 如果name不存在, 不会报错, 而是返回None或默认值, 如果有多个只会返回一个
    print(request.GET.getlist('name'))  # 如果name有多个值, 则都会获取
    print('*'*60)
    print(request.path)  # 路径
    print(request.get_full_path())
    print('*'*60)
    print(request.COOKIES)  # 会话技术
    print(request.session)  # 会话技术
    print('*'*60)
    print(request.FILES)  # 文件, 前端上传的文件对象
    print(request.META['REMOTE_ADDR'])  # 远程地址: 客户端的IP地址
    return HttpResponse('OK')

def my_response(request):
    # 1. 返回字符串: 企业项目中使用很少
    response = HttpResponse('OK')
    response.content = 'hello'
    response.status_code = 400
    return response
    # 2. 返回模板: 前后端不分离的情况下使用
    # return render(request, 'index.html')

    # 3. 重定向: 页面跳转
    # return redirect('/request/')

    # 4. 返回JSON: 前后端分离
    # return JsonResponse({'data': 'hello world'})























