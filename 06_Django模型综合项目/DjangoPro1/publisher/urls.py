from django.urls import path
from publisher.views import *

urlpatterns = [
    path('detail/<int:pid>/', publisher_detail, name='detail'),
]