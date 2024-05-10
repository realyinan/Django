from django.urls import path
from author.views import *

urlpatterns = [
    path('detail/<int:aid>/', author_detail, name='detail')
]