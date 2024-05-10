import math

from django.db.models import Max, Min, Sum, Avg, Count
from django.shortcuts import render, HttpResponse
# 导入models
from App.models import *

# 增加数据
def add_person(request):
    # 方式1
    # try:
    #     p = PersonModel()
    #     p.name = '李四'
    #     p.age = 33
    #     p.save()  # 同步到数据库表中
    # except Exception as e:
    #     return HttpResponse('add fail')
    # return HttpResponse('add ok')

    # 方式2
    # try:
    #     p = PersonModel(name='王五', age=20)
    #     p.save()  # 同步到数据库表中
    # except Exception as e:
    #     return HttpResponse('add fail')
    # return HttpResponse('add ok')

    # 方式3
    # try:
    #     p = PersonModel.objects.create(name='赵六', age=20)
    # except Exception as e:
    #     return HttpResponse('add fail')
    # return HttpResponse('add ok')

    # 方式4
    # try:
    #     ret = PersonModel.objects.get_or_create(name='钱七', age=20)
    #     print('ret', ret)
    #     # 第一次创建就是true, 如果已经存在则是false
    # except Exception as e:
    #     return HttpResponse('add fail')
    # return HttpResponse('add ok')

    # 添加多条数据
    for i in range(26, 100):
        PersonModel.objects.create(name=f'胡{i}铃', age=i)
    return HttpResponse('add ok')


# 删除数据
# 1. 先找到要删除的数据
# 2. 然后删除
def del_person(request):
    # 删除一条数据
    # try:
    #     p = PersonModel.objects.first()  # 第一条数据
    #     p.delete()
    # except Exception as e:
    #     return HttpResponse('删除失败')
    #
    # return HttpResponse('删除成功')

    # 删除多条数据
    try:
        PersonModel.objects.filter(age__gt=15).delete()
    except Exception as e:
        return HttpResponse('删除失败')

    return HttpResponse('删除成功')


# 修改数据
# 1. 先找到要修改的数据
# 2. 然后修改
def update_person(request):
    # 修改一条数据
    try:
        p = PersonModel.objects.first()
        p.age = 666
        # p.save()
        p.save(update_fields=['age'])  # 指定更新的字段, 提高更新的效率
    except Exception as e:
        return HttpResponse('修改失败')
    return HttpResponse('修改成功')

    # 修改多条数据
    # try:
    #     PersonModel.objects.all().update(age=100)
    # except Exception as e:
    #     return HttpResponse('修改失败')
    # return HttpResponse('修改成功')


# 查询数据
def get_person(request):
    # get(): 得到一个对象(一条数据)
    # 如果没有找到符合条件的对象，会引发模型类.DoesNotExist异常
    # 如果找到多个，会引发模型类.MultipleObjectsReturned 异常
    # p = PersonModel.objects.get(id=16)
    # p = PersonModel.objects.get(pk=16)  # pk: primary key
    # p = PersonModel.objects.get(age=666)
    # p = PersonModel.objects.get(age=100)  # MultipleObjectsReturned
    # p = PersonModel.objects.get(age=1666)  # DoesNotExist
    # print('*' * 60)
    # print(p, type(p))
    # print(p.name, p.age)
    # print('*' * 60)

    # all(): 获取所有数据 返回QuerySet 查询集
    persons = PersonModel.objects.all()
    print(persons, type(persons))
    # 可以遍历查询集
    for p in persons:
        print(p.name, p.age)

    # first(): 第一条数据
    p = PersonModel.objects.first()
    print(p.name, p.age)

    # last(): 最后一条数据
    p = PersonModel.objects.last()
    print(p.name, p.age)

    # filter(): 过滤, 使用最多, 返回的是查询集
    persons = PersonModel.objects.filter()  # 默认没有条件, 得到所有数据
    persons = PersonModel.objects.filter(age__gt=300)  # age>300
    persons = PersonModel.objects.filter(age__gte=300)  # age>=300
    persons = PersonModel.objects.filter(age__lt=300)  # age<300
    persons = PersonModel.objects.filter(age__lte=300)  # age<=300
    persons = PersonModel.objects.filter(age=300)  # age=300
    print(persons, type(persons))
    for p in persons:
        print('----', p.name, p.age)
    # 查询集可以做链式调用
    print(persons.first())
    print(persons.last())
    print(persons.exists())  # 查询集是否存在, 如果存在则为true, 否则为false
    print(persons.count())  # 查询集中的数据个数

    persons = PersonModel.objects.filter()
    print("persons:", persons)
    print("list(persons):", list(persons))  # 将查询集强制转换为列表
    # values(): 列表套字典, 包括字段和值
    print("persons.values():", persons.values())  # 列表套字典的方式
    print("persons.values('name, age'):", persons.values('name', 'age'))
    # values_list(): 列表套元组, 只包括值
    print("persons.values_list('name, age'):", persons.values_list('name', 'age'))  # 列表套元组
    print('-'*60)

    # filter(): 详细, 类似数据库中的where语句
    persons = PersonModel.objects.filter(age__in=[100, 200, 666, 777, 888])
    persons = PersonModel.objects.exclude(age__in=[100, 200, 666, 777, 888])  # 排除的意思
    persons = PersonModel.objects.filter(age__contains='6')  # 包含, 模糊查找, 类似SQL中的like
    persons = PersonModel.objects.filter(name__icontains='3')
    persons = PersonModel.objects.filter(name__regex='^hu')  # 正则匹配
    persons = PersonModel.objects.filter(name__iregex='^hu')  # 正则忽略大小写
    persons = PersonModel.objects.filter(age__range=[100, 500])  # 100-500之间, 两边都包含
    persons = PersonModel.objects.filter(name__startswith='hu')  # 以wu开头, 忽略大小写
    persons = PersonModel.objects.filter(name__endswith='铃')  # 以铃结尾,
    print("persons:", persons)

    # 聚合函数: max, min, sum
    res = PersonModel.objects.aggregate(Max('age'))  # 最大值
    res = PersonModel.objects.aggregate(Min('age'))  # 最小值
    res = PersonModel.objects.aggregate(Sum('age'))  # 求和
    res = PersonModel.objects.aggregate(Avg('age'))  # 平均值
    res = PersonModel.objects.aggregate(Count('id'))
    print(res)

    # 排序
    persons = PersonModel.objects.all().order_by('age')  # 升序
    persons = PersonModel.objects.all().order_by('-age', 'id')  # 先按age降序, 如果age相同则按id升序排列
    print(persons)

    return HttpResponse('查询成功')

# 手动分页功能
def pageinate(request, page=1):
    # 页码: page
    # 每页数量; per_page
    per_page = 10
    persons = PersonModel.objects.all()
    persons = persons[(page - 1) * per_page: page * per_page]

    # 总页数
    total = PersonModel.objects.count()  # 总数据
    total_page = math.ceil(total / per_page)  # 总页数
    pages = range(1, total_page+1)

    return render(request, 'pageinate.html', {'persons': persons, 'pages': pages})

# 分页器
from django.core.paginator import Paginator


def pageinate2(request, page=1):
    per_page = 10
    all_data = PersonModel.objects.all()

    paginator = Paginator(all_data, per_page)
    persons = paginator.page(page)  # 获取第page页的数据
    pages = paginator.page_range  # 属性 页码的范围, 可以遍历的

    return render(request, 'pageinate2.html', {'persons': persons, 'pages': pages})






























