from django.shortcuts import render, HttpResponse
from One2One.models import *

# 查询
def get(request):
    # 查找某用户的身份证信息
    user = User.objects.get(pk=1)
    print(user.idcard)
    print(user.idcard.idcard_num, user.idcard.address)
    print('*'*60)
    # 查找身份证对应的用户
    idcard = IDCard.objects.get(pk=1)
    print(idcard.user)
    print(idcard.user.name, idcard.user.age, idcard.user.sex)
    return HttpResponse('查询成功')
