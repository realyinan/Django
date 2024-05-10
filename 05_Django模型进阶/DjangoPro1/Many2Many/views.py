from django.shortcuts import render, HttpResponse
from Many2Many.models import *

# 多对多

# 增加数据
def add(request):
    # 添加User
    # for i in range(1, 10):
    #     User.objects.create(name=f'张三{i}', age=i)

    # 添加Movie
    # for i in range(1, 10):
    #     Movie.objects.create(name=f'阿凡达{i}', duration=100+i)

    # 添加中间表数据
    user = User.objects.get(name='张三1')  # 获取用户
    movie = Movie.objects.get(name='阿凡达2')  # 获取电影

    # user.movies.add(movie)  # 用户收藏电影
    movie.user_set.add(user)  # 反向
    return HttpResponse('增加成功')

def delete(request):
    # 删除User
    # User.objects.filter(pk=9).delete()

    # 删除Movie
    # Movie.objects.filter(id=9).delete()

    # 删除中间表
    user = User.objects.get(name='张三1')
    user.movies.filter(name='阿凡达3').delete()
    return HttpResponse('删除成功')

def get_user_movie(request):
    # 获取用户收藏的所有电影
    user = User.objects.get(id=1)
    print(user.movies.all())
    # 反向获取电影被那些用户所收藏
    movie = Movie.objects.get(id=4)
    print(movie.user_set.all())
    return HttpResponse('查询成功')


