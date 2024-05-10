import os
import uuid

from django.shortcuts import render, redirect, reverse
from django.conf import settings

from App.models import *


# 静态文件的使用
def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

# 上传文件: 媒体文件
def upload1(request):
    if request.method == 'GET':
        return render(request, 'upload1.html')
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        icon = request.FILES.get('icon')  # 单个文件
        # print(icon, type(icon))
        # 1.jpg <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
        # print(icon.name)  # 1.jpg

        # 1. 将上传的图片存储到后台对应的媒体文件中
        file_name = gen_uuid_name() + os.path.splitext(icon.name)[-1]  # 接受一个路径作为参数，并返回一个元组，其中第一个元素是路径（不包括扩展名），第二个元素是扩展名
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)

        with open(file_path, 'ab') as fp:
            for part in icon.chunks():
                fp.write(part)
                fp.flush()  # 清空缓存
        # 2. 将该媒体文件的路径, 存入到数据库中
        user = UserModel()
        user.name = uname
        user.icon = 'uploads/' + file_name
        user.save()

        return redirect(reverse('showicon'))

# 通过uuid来得到唯一的图片名称
def gen_uuid_name():
    return str(uuid.uuid4())

# 显示图片
def show_icon(request):
    user = UserModel.objects.get(pk=2)
    return render(request, 'showicon.html', {'user': user})

# 多文件上传
def upload2(request):
    if request.method == 'GET':
        return render(request, 'upload2.html')
    elif request.method == 'POST':
        # 接受前端提交过来的数据
        uname = request.POST.get('uname')
        imgs = request.FILES.getlist('imgs')
        for img in imgs:
            # 1. 把图片存储到uploads中
            file_name = gen_uuid_name() + os.path.splitext(img.name)[-1]
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            with open(file_path, 'ab') as fp:
                for part in img.chunks():
                    fp.write(part)
                    fp.flush()

            # 2.将图片路径存入到数据库中
            photo = PhotoModel()
            photo.img = 'uploads/' + file_name
            photo.user = UserModel.objects.filter(name=uname).first()
            photo.save()


        return redirect(reverse('showicon'))

