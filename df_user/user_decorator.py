#coding=utf-8
from django.http import HttpResponseRedirect

def login(func):
    def login_fun(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url',request.get_full_path()) #从哪里来到哪里去
            # request.path:表示当前路径
            # request.get_full_path():表示完整路径
            return red
    return login_fun