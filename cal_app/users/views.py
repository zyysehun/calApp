from curses.ascii import NUL
from django_redis import get_redis_connection
from pymysql import NULL
from utils.views import LoginRequiredJSONMixin
from django.shortcuts import render
from users.models import User
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import logout
import json
import re

# Create your views here.


class UsernameCountView(View):

    def get(self, request, username):
        # 1.  接收用户名，对这个用户名进行一下判断
        # if not re.match('[a-zA-Z0-9_-]{5,20}',username):
        #     return JsonResponse({'code':200,'errmsg':'用户名不满足需求'})
        # 2.  根据用户名查询数据库
        count = User.objects.filter(username=username).count()
        # 3.  返回响应
        return JsonResponse({'code': 0, 'count': count, 'errmsg': 'ok'})


class RegisterView(View):

    def post(self, request):
        # 1. 接收请求（POST------JSON）
        body_unicode = request.body.decode()
        body = json.loads(body_unicode, strict=False)
        content = body['content']

        print(content)

    # 2. 获取数据
    # username = body_dict.get('username')
    # password = body_dict.get('password')
    # password2 = body_dict.get('password2')
    #  mobile = body_dict.get('mobile')
    #   print(username)
       # allow = body_dict.get('allow')

       # 3. 验证数据
       #     3.1 用户名，密码，确认密码，手机号，是否同意协议 都要有
       # all([xxx,xxx,xxx])
       # all里的元素 只要是 None,False
       # all 就返回False，否则返回True
    #    if not all([username, password, password2, mobile]):
    #         return JsonResponse({'code': 400, 'errmsg': '参数不全'})
    #     #     3.2 用户名满足规则，用户名不能重复
    #     if not re.match('[0-9a-zA-Z_-]{5,20}', username):
    #         return JsonResponse({'code': 400, 'errmsg': '用户名不满足规则'})
        #     3.3 密码满足规则
        #     3.4 确认密码和密码要一致
        #     3.5 手机号满足规则，手机号也不能重复
        #     3.6 需要同意协议
        # 4. 数据入库
        # user = User(username=username, password=password, mobile=mobile)
        # user.save()

        # User.objects.create(username=username,password=password,mobile=mobile)

        # 如何设置session信息
        # request.session['user_id'] = user.id

        # 5. 返回响应
        return JsonResponse({'code': 0, 'errmsg': 'ok'}, safe=False)


def Register(request):
    # 1. 接收请求（POST------JSON）
    body_bytes = request.body
    body_str = body_bytes.decode()
    body_dict = json.loads(body_str)

    # 2. 获取数据
    username = body_dict.get('username')
    password = body_dict.get('password')
    password2 = body_dict.get('password2')
    mobile = body_dict.get('mobile')
    print(username)

    if not all([username, password, password2, mobile]):
        return JsonResponse({'code': 400, 'errmsg': '参数不全'})
    if not re.match('[0-9a-zA-Z_-]{5,20}', username):
        return JsonResponse({'code': 400, 'errmsg': '用户名不满足规则'})

    # 数据入库
    user = User(username=username, password=password, mobile=mobile)
    user.save()

    # 如何设置session信息
    # request.session['user_id'] = user.id

    data = {'code': 0, 'errmsg': 'ok'}
    return JsonResponse(data=data, safe=False)


def Login(request):
    # 1. 接收数据
    data = json.loads(request.body.decode())
    username = data.get('username')
    password = data.get('password')
    remembered = data.get('remembered')

    # 2. 验证数据
    if not all([username, password]):
        return JsonResponse({'code': 400, 'errmsg': '参数不全'})

    # from django.contrib.auth import authenticate
    # # authenticate 传递用户名和密码
    # # 如果用户名和密码正确，则返回 User信息
    # # 如果用户名和密码不正确，则返回 None
    # user = authenticate(username=username, password=password)

    # if user is None:
    #     return JsonResponse({'code': 400, 'errmsg': '账号或密码错误'})

    # 3.查询
    user = User.objects.filter(
        username=username, password=password).exclude(status=9)
    if not user:
        response = JsonResponse(
            {'code': 404, 'errmsg': '密码或用户名错误'})
    else:
        response = JsonResponse({'code': 0, 'errmsg': 'ok'})
    return response


def index(request):
    '''浏览信息'''
    try:
        name = request.GET['query']
        # print(name)
        umod = User.objects.filter(username__contains=name)
        count = umod.count()
        # print(count)
        dict = {}
        json_data = [{'id': umods.id, 'username': umods.username, 'password': umods.password,
                      'mobile': umods.mobile, 'status': umods.status} for umods in umod]
    # print(json_data)

    # ulist = umod.filter(status__lt=9)
    # data = [{'id': blog.pk, 'name': blog.name} for blog in blogs]

    # responseDate = {'data': json_data,
    # 'code': '200', 'message': '获取成功!'}
        response = JsonResponse(
            {'data': json_data, 'code': 200, 'errmsg': 'ok', 'count': count})
    except Exception as err:
        print(err)
        response = JsonResponse(
            {'code': 404, 'errmsg': 'faile'})
    return response


def addUser(request):
    try:
      # 1. 接收数据
        data = json.loads(request.body.decode())
        username = data.get('username')
        password = data.get('password')
        mobile = data.get('mobile')
        print(username)
        if not all([username, password, mobile]):
            return JsonResponse({'code': 400, 'errmsg': '参数不全'})
        if not re.match('[0-9a-zA-Z_-]{5,20}', username):
            return JsonResponse({'code': 400, 'errmsg': '用户名不满足规则'})

        # 数据入库
        user = User(username=username, password=password, mobile=mobile)
        user.save()

        response = JsonResponse(
            {'code': 200, 'errmsg': 'ok'})
    except Exception as err:
        print(err)
        response = JsonResponse(
            {'code': 404, 'errmsg': 'faile'})
    return response


def showEditDialog(request, id):
    try:
        user = User.objects.get(id=id)
        # print(user)

        data = {'id': user.id, 'username': user.username,
                'mobile': user.mobile, 'password': user.password}

        # 3.  返回响应
        response = JsonResponse(
            {'data': data, 'code': 200, 'errmsg': 'ok'})
    except Exception as err:
        print(err)
        response = JsonResponse(
            {'code': 404, 'errmsg': 'faile'})
    return response


def editUser(request, uid):
    '''执行信息编辑'''
    try:
        data = json.loads(request.body.decode())
        mobile = data.get('mobile')
        ob = User.objects.get(id=uid)
        ob.mobile = mobile
        ob.save()
        data = {'id': ob.id, 'username': ob.username,
                'mobile': ob.mobile, 'password': ob.password}
        response = JsonResponse(
            {'data': data, 'code': 200, 'errmsg': 'ok'})
    except Exception as err:
        print(err)
        response = JsonResponse(
            {'code': 404, 'errmsg': 'faile'})
    return response


def delete(request, uid):
    '''执行信息删除'''
    try:
        ob = User.objects.get(id=uid)
        ob.status = 9
        ob.save()
        response = JsonResponse(
            {'code': 200, 'errmsg': 'ok'})
    except Exception as err:
        print(err)
        response = JsonResponse(
            {'code': 404, 'errmsg': 'faile'})
    return response
