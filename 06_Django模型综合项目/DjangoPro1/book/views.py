from django.shortcuts import render
from book.models import *

# 书籍首页
def book_index(request):
    return render(request, 'book/book_index.html')

# 书籍列表页
def book_list(request):
    # 获取所有书籍数据
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

# 书籍详情页
def book_detail(request, bid):
    # 获取bid对应的书籍
    book = Book.objects.get(pk=bid)
    return render(request, 'book/book_detail.html', {'book': book})