from django.shortcuts import render, HttpResponse, redirect
from django.views import View


class LoginView(View):


    def dispatch(self, request, *args, **kwargs):
        # 服务端接受到用户的请求, 判断从session中是否能取到用户状态信息,若取不到则返回登录页面
        print('login before')
        if request.path == '/login/':
            # 若此次请求的url是登录的话,则继续正常执行
            ret = super(LoginView, self).dispatch(request, *args, **kwargs)
            print('login after')
            return ret

        if not request.session.get('user_info'): # 若此时未登录,则会陷入死循环, 运行到11行就会返回
            return redirect('/login/')

    def get(self, request):
        return render(request, 'login.html')

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
        print('index before')
        if not request.session.get('user_info'):
            return redirect('/login/')
        print('index after')

        ret = super(IndexView, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request):
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        return redirect('/index/')

    elif request.method == 'GET':
        return render(request, 'register.html')


