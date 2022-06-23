import decimal
import json
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator

from upload.models import Cal, Cal02, Cal03, Calhim


# Create your views here.

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def findData(request):
    # pagenum = request.GET['pagenum']
    # pagesize = request.GET['pagesize']
    datetimequery = request.GET['query']
    # print(type(datetimequery))
    print(datetimequery)
    # print(pagenum)
    # print(pagesize)
    cmod = Cal.objects
    # list = cmod.get(wavelength = 430)
    # sqlOrder = get_object_or_404(SqlOrder,id=cmod.get('id'))
    # objJson = serialize('json',[sqlOrder])[1:-1]
    # data = cmod.all().filter(wavelength = 423).values()
    try:
        data = cmod.filter(datetime__startswith=datetimequery[0:16]).values()
        # if data.length == 0:
        #     responseDate = {'data': 0, 'code': '404', 'message': '沒有找到!'}
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到!'}
        else:
            json_data = list(data)
            json_data = json.dumps(
                json_data, cls=DateEncoder, ensure_ascii=False)
            # print(json_data)
            # print(type(json_data))

            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}

    # data = {'data': 'ceshi','code': '200','message':'获取成功!'}
    return JsonResponse(responseDate)


def showImage(request):
    datetimequery = request.GET['query']
    cmod = Cal.objects
    wavelength = []
    raddata = []
    try:
        data = cmod.filter(datetime__startswith=datetimequery[0:16]).values(
            "wavelength", "caldata")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到!'}
        else:
            json_data = list(data)
            json_data = json.dumps(
                json_data, cls=DateEncoder, ensure_ascii=False)
            print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
            # print(json_data)
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def findData02(request):

    datetimequery = request.GET['query']
    print(datetimequery)
    cmod = Cal02.objects
    try:
        data = cmod.filter(datetime__startswith=datetimequery[0:16]).values()
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到!'}
        else:
            json_data = list(data)
            json_data = json.dumps(
                json_data, cls=DateEncoder, ensure_ascii=False)
            # print(json_data)
            # print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}

    # data = {'data': 'ceshi','code': '200','message':'获取成功!'}
    return JsonResponse(responseDate)


def showImage02(request):
    datetimequery = request.GET['query']
    cmod = Cal02.objects
    wavelength = []
    raddata = []
    try:
        data = cmod.filter(datetime__startswith=datetimequery[0:16]).values(
            "wavelength", "caldata")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到!'}
        else:
            json_data = list(data)
            json_data = json.dumps(
                json_data, cls=DateEncoder, ensure_ascii=False)
            print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
            # print(json_data)
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def findData03(request):

    datetimequery = request.GET['query']
    print(datetimequery)
    cmod = Cal03.objects
    try:
        data = cmod.filter(datetime__startswith=datetimequery[0:16]).values()
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到!'}
        else:
            json_data = list(data)
            json_data = json.dumps(
                json_data, cls=DateEncoder, ensure_ascii=False)
            # print(json_data)
            # print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}

    # data = {'data': 'ceshi','code': '200','message':'获取成功!'}
    return JsonResponse(responseDate)


def showImage03(request):
    datetimequery = request.GET['query']
    cmod = Cal03.objects
    wavelength = []
    raddata = []
    try:
        data = cmod.filter(datetime__startswith=datetimequery[0:16]).values(
            "wavelength", "caldata")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到!'}
        else:
            json_data = list(data)
            json_data = json.dumps(
                json_data, cls=DateEncoder, ensure_ascii=False)
            print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
            # print(json_data)
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def findDataHIM(request):
    datetimequery = request.GET['query']
    print(datetimequery)
    cmod = Calhim.objects
    try:
        data = cmod.filter(datetime__startswith=datetimequery[0:17]).values()
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到!'}
        else:
            json_data = list(data)
            json_data = json.dumps(
                json_data, cls=DateEncoder, ensure_ascii=False)
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def showImageHIM(request):
    datetimequery = request.GET['query']
    cmod = Calhim.objects
    try:
        data = cmod.filter(datetime__startswith=datetimequery[0:16]).values(
            "wavelength", "diff", "global_irr", "direct", "dg_radio")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到!'}
        else:
            json_data = list(data)
            json_data = json.dumps(
                json_data, cls=DateEncoder, ensure_ascii=False)
            print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
            # print(json_data)
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)
