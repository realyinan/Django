from django.shortcuts import render
from author.models import *

# 作者详情
def author_detail(request, aid):
    # 获取aid对应的作者
    author = Author.objects.get(pk=aid)
    return render(request, 'author/author_detail.html', {'author': author})
