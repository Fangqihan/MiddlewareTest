# -*- coding: utf-8 -*-   @Time    : 18-1-25 下午6:58
# @Author  : QiHanFang    @Email   : qihanfang@foxmail.com

from django.shortcuts import HttpResponse, redirect

class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class Md1(MiddlewareMixin):
    def process_request(self, request):
        print('md1_process_request')
        # print(request.path)
        #  若本次请求的是login页面,则直接往下执行
        if request.path == '/login/':
            return None
        #  若本次请求的是login页面,则要判断用户当前登录信息状态,
        # 若未登录则返回登录页面
        # if not request.session.get('user_info1',''):
        #     return redirect('/login/')

    def process_response(self, request, response):
        print('md1_process_response')
        return response  # 必须带返回值

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('Md1_process_view')
        # return HttpResponse('我返回')

    def process_exception(self, request, exception):
        print('Md1_process_exception')
        # return HttpResponse('程序有误')

    def process_template_response(self, request, response):
        print('md1_process_template_response')

class Md2(MiddlewareMixin):
    def process_request(self, reqeust):
        print('md2_process_request')
        pass

    def process_response(self, requst, response):
        print('md2_process_response')
        return response  # 必须带返回值

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('Md2_process_view')

    def process_exception(self, request, exception):
        print('Md2_process_exception')
        # return HttpResponse('程序有误')

    def process_template_response(self, request, response):
        print('md2_process_template_response')
        return HttpResponse('asdasdasd')
