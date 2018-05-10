# coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
from hashlib import sha1
from .models import *

def register(request):
    context = {'title': 'T注册用户'}
    return render(request, 'df_user/register.html',context)

def register_handle(request):
    # 获取请求参数
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    # 判断两次密码是否相等式（防止特殊情况）
    if upwd != upwd2:
        return redirect('/user/register/')

    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    pwd = s1.hexdigest()

    #创建模型
    user = UserInfo()
    user.uname = uname
    user.upwd = pwd
    user.uemail = uemail
    user.save()# 保存到数据库中

    # 记录在session中，在login页面写入
    request.session['reg_uname'] = uname

    # 注册成功，转到登录页
    return redirect('/user/login')

def login(request):
    # 从注册页面保存一个session
    username = request.session.get('reg_uname',default='')
    if username == '':
        # 获取cookies值，未获得默认为''
        username = request.COOKIES.get('uname', '')
    else:# 注册页面保存的只用一次，用过即删
        del request.session['reg_uname']

    loc_uremember_username = request.COOKIES.get('uremember_username', '')
    context = {
        'title': 'T用户登录',
        'errorname': 0,
        'errorpassword': 0,
        'username': username,
        'remember_username': loc_uremember_username
    }
    return render(request, 'df_user/login.html', context)

def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd','')
    if upwd == '':
        redirect('/user/login')
    # 是否记住用户名,设置默认值为on 表示勾选记住用户名
    uremember_username = post.get('remember_username','on')

    # 加密后与数据库中存储的值对比
    s1 = sha1()
    s1.update(upwd)
    pwd = s1.hexdigest()
    # 查询数据库中的密码
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 0:
        context = {
            'title': 'T用户登录',
            'errorname': 1,# 用户名错误
            'errorpassword': 0,
            'username': '',
            'remember_username': uremember_username
        }
        return render(request, 'df_user/login.html', context)

    # 密码错误重新登录
    if users[0].upwd != pwd:
        context = {
            'title': 'T用户登录',
            'errorname': 0,
            'errorpassword': 1,# 密码错误
            'username': uname,
            'remember_username': uremember_username
        }
        return render(request, 'df_user/login.html', context)

    # 创建response来设置cookie（存于客户端）
    red = HttpResponseRedirect('/user/user_center')
    if uremember_username == 'on':
        red.set_cookie('uname', uname)
        red.set_cookie('uremember_username', 'on')
    else:# 设置为‘’，并立即过期
        red.set_cookie('uname', '', max_age=-1)
        red.set_cookie('uremember_username', '', max_age=-1)
    return red

def user_center_info(request):
    context = {'title': 'T个人信息'}
    return render(request, 'df_user/user_center_info.html', context)

def user_center_order(request):
    context = {'title': 'T全部订单'}
    return render(request, 'df_user/user_center_order.html', context)

def user_center_site(request):
    context = {'title': 'T收货地址'}
    return render(request, 'df_user/user_center_site.html', context)

# ajax
def username_exist(request):
    uname = request.GET['user_name']
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})