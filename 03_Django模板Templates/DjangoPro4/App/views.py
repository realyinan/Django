from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'name': '张三'})
