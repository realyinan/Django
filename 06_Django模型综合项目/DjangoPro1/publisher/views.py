from django.shortcuts import render
from publisher.models import *

# 出版社详情
def publisher_detail(request, pid):
    # 获取pid对应的出版社数据
    publisher = Publisher.objects.get(pk=pid)
    return render(request, 'publisher/publisher_detail.html', {'publisher': publisher})
