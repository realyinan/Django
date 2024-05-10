from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 子路由, 使用命名空间
    path('author/', include(('author.urls', 'author'), namespace='author')),
    path('book/', include(('book.urls', 'book'), namespace='book')),
    path('publisher/', include(('publisher.urls', 'publisher'), namespace='publisher')),

    path('admin/', admin.site.urls),
]

# 1.在书籍的book_index.html中有⼀个"查看所有书籍"的超链接按钮，点击进⼊书籍列表book_list.html⻚⾯.
# 2.在书籍的book_list.html中显示所有书名，点击书名可以进⼊书籍详情book_detail.html（通过书籍id）
# 3.在书籍book_detail.html中可以点击该书的作者和出版社，进⼊作者详情的author_detail.html和出版社详情的publisher_detail.html⻚⾯