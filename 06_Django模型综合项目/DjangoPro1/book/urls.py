from django.urls import path
from book.views import *

urlpatterns = [
    path('index/', book_index, name='index'),
    path('list/', book_list, name='list'),
    path('detail/<int:bid>/', book_detail, name='detail'),
]