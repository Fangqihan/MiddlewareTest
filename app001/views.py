from django.shortcuts import render, HttpResponse, redirect
from django.views import View

# class AuthView(View):
#     def dispatch(self, request, *args, **kwargs):
#         # 若此次请求的url是登录的话,则继续正常执行
#         # if request.path == '/login/':
#         #     return None
#
#         # 用户未登录则返回登录界面
#         if not request.session.get('user_info'):
#             return redirect('/login/')
#
#         ret = super(AuthView, self).dispatch(request, *args, **kwargs)
#         return ret
#
#
# class LoginView(AuthView):
#     def get(self, request):
#         return render(request, 'login.html')
#
#     def post(self, request):
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         if username == 'alex' and password == 'abc123':
#             request.session['user_info'] = 'alex'
#             return redirect('/index/')
#         else:
#             return render(request, 'login.html')
#
#
# class IndexView(AuthView):
#     def get(self, request):
#         return render(request, 'index.html')

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# @装饰函数后,那么当以post请求启用此函数时候,可以不带csrf

def test(func):
    """装饰器函数"""
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner


# @method_decorator(test, name='get')
#  方式1:可以指定作用的函数名称
class LoginView(View):

    # @method_decorator(test)
    # 方式2: 对post和get函数都产生作用
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # 服务端接受到用户的请求, 判断从session中是否能取到用户状态信息,若取不到则返回登录页面
        # 若此次请求的url是登录的话,则继续正常执行
        if request.path == '/login/':
            ret = super(LoginView, self).dispatch(request, *args, **kwargs)
            # print('login after')
            return ret

        if not request.session.get('user_info'): # 若此时未登录,则会陷入死循环, 运行到11行就会返回
            return redirect('/login/')

    # @method_decorator(test)
    # 方式3: 仅仅作用域get函数
    def get(self, request):
        return render(request, 'login.html')

    # @method_decorator(csrf_exempt)
    # BUG 之一,放在此处不行
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'alex' and password == 'abc123':
            request.session['user_info'] = 'alex'
            return redirect('/index/')
        else:
            return render(request, 'login.html')


class IndexView(View):
    def dispatch(self, request, *args, **kwargs):
        # 服务端接受到用户的请求, 判断从session中是否能取到用户状态信息,若取不到则返回登录页面
        # print('index before')
        if not request.session.get('user_info'):
            return redirect('/login/')
        # print('index after')

        ret = super(IndexView, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request):
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        return redirect('/index/')

    elif request.method == 'GET':
        return render(request, 'register.html')


def tes(request):
    return HttpResponse('你好')