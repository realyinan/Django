import datetime

from django.shortcuts import render

def index(request):
    data = {
        'name': 'zhangsan',
        'age': 40,
        'likes': ['movie', 'game', 'code'],
        'address': {'city': '深圳', 'province': '广东'},
        'stars': [
            ['马化腾', '马云', '马斯克'],
            ['雷军', '李彦宏', '张一鸣'],
            ['扎克伯格', '比尔盖茨', '谢尔盖布林']
        ],
        'dt': datetime.datetime.now(),
        'code': '<b>I am a goodman</b>',
        'code2': '''<script>
                        var n = 3
                        while (n--) {
                        alert('哈哈')
                        }
                    </script>'''
    }
    return render(request, 'index.html', data)

# 模板继承
# 父模板
def block(request):
    return render(request, 'block.html')

# 子模版
def child(request):
    return render(request, 'child.html')
