import decimal
import json
import datetime
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator

from upload.models import Cal, Cal02, Cal03, Calhim, Spec01, Spec02, Spec03, Psrv1, Psrv2

"""
def showImage(request):
    datetimequery = request.GET['query']
    cmod = Cal.objects
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    try:
        data = cmod.filter(datetime__startswith=datetimequery[0:16]).values(
            "wavelength", "caldata")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
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
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    cmod = Cal02.objects
    try:
        data = cmod.filter(datetime__startswith=datetimequery[0:16]).values()
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
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
"""

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
    datetimequery = request.GET['query']
    date1 = datetimequery[0:10]
    time1 = datetimequery[11:19]
    print(date1)
    print(time1)
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    cmod = Cal.objects
    try:
        # data = cmod.filter(datetime__startswith=datetimequery[0:16]).values()
        data = cmod.filter(date=date1).filter(
            time__startswith=time1[0:5]).values()
        # filter(time__startswith=time).
        print(data)
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            #  json.dumps(your_data, default=str)
            # json_data = json.dumps(
            #     json_data, cls=DateEncoder, ensure_ascii=False)
            json_data = json.dumps(json_data, default=str)
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def showImage(request):
    datetimequery = request.GET['query']
    date = datetimequery[0:10]
    time = datetimequery[11:19]
    cmod = Cal.objects
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    try:
        data = cmod.filter(date=date).filter(
            time__startswith=time[0:5]).values("wavelength", "caldata")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            json_data = json.dumps(json_data, default=str)
            # print(type(json_data))
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
    date1 = datetimequery[0:10]
    time1 = datetimequery[11:19]
    print(date1)
    print(time1)
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    cmod = Cal02.objects
    try:
        # data = cmod.filter(datetime__startswith=datetimequery[0:16]).values()
        data = cmod.filter(date=date1).filter(
            time__startswith=time1[0:5]).values()
        # filter(time__startswith=time).
        print(data)
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            #  json.dumps(your_data, default=str)
            # json_data = json.dumps(
            #     json_data, cls=DateEncoder, ensure_ascii=False)
            json_data = json.dumps(json_data, default=str)
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def showImage02(request):
    datetimequery = request.GET['query']
    date = datetimequery[0:10]
    time = datetimequery[11:19]
    cmod = Cal02.objects
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    try:
        data = cmod.filter(date=date).filter(
            time__startswith=time[0:5]).values("wavelength", "caldata")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            json_data = json.dumps(json_data, default=str)
            # print(type(json_data))
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
    date1 = datetimequery[0:10]
    time1 = datetimequery[11:19]
    print(date1)
    print(time1)
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    cmod = Cal03.objects
    try:
        # data = cmod.filter(datetime__startswith=datetimequery[0:16]).values()
        data = cmod.filter(date=date1).filter(
            time__startswith=time1[0:5]).values()
        # filter(time__startswith=time).
        print(data)
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            #  json.dumps(your_data, default=str)
            # json_data = json.dumps(
            #     json_data, cls=DateEncoder, ensure_ascii=False)
            json_data = json.dumps(json_data, default=str)
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def showImage03(request):
    datetimequery = request.GET['query']
    date = datetimequery[0:10]
    time = datetimequery[11:19]
    cmod = Cal03.objects
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    try:
        data = cmod.filter(date=date).filter(
            time__startswith=time[0:5]).values("wavelength", "caldata")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            json_data = json.dumps(json_data, default=str)
            # print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
            # print(json_data)
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)

# Calhim


def findDataHIM(request):
    datetimequery = request.GET['query']
    date1 = datetimequery[0:10]
    time1 = datetimequery[11:19]
    print(date1)
    print(time1)
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    cmod = Calhim.objects
    try:
        # data = cmod.filter(datetime__startswith=datetimequery[0:16]).values()
        data = cmod.filter(date=date1).filter(
            time__startswith=time1[0:5]).values()
        # filter(time__startswith=time).
        print(data)
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            #  json.dumps(your_data, default=str)
            # json_data = json.dumps(
            #     json_data, cls=DateEncoder, ensure_ascii=False)
            json_data = json.dumps(json_data, default=str)
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def showImageHIM(request):
    datetimequery = request.GET['query']
    date = datetimequery[0:10]
    time = datetimequery[11:19]
    cmod = Calhim.objects
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    try:
        data = cmod.filter(date=date).filter(
            time__startswith=time[0:5]).values("wavelength", "diff", "global_irr", "direct", "dg_radio")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            json_data = json.dumps(json_data, default=str)
            # print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
            # print(json_data)
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def findDataSpec01(request):
    datetimequery = request.GET['query']
    date1 = datetimequery[0:10]
    time1 = datetimequery[11:19]
    print(date1)
    print(time1)
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    cmod = Spec01.objects
    try:
        # data = cmod.filter(datetime__startswith=datetimequery[0:16]).values()
        data = cmod.filter(date=date1).filter(
            time__startswith=time1[0:5]).values()
        # filter(time__startswith=time).
        print(data)
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            #  json.dumps(your_data, default=str)
            # json_data = json.dumps(
            #     json_data, cls=DateEncoder, ensure_ascii=False)
            json_data = json.dumps(json_data, default=str)
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def showImageSpec01(request):
    datetimequery = request.GET['query']
    date = datetimequery[0:10]
    time = datetimequery[11:19]
    cmod = Spec01.objects
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    try:
        data = cmod.filter(date=date).filter(
            time__startswith=time[0:5]).values("wavelength", "reflectance")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            json_data = json.dumps(json_data, default=str)
            # print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
            # print(json_data)
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def findDataSpec02(request):
    datetimequery = request.GET['query']
    date1 = datetimequery[0:10]
    time1 = datetimequery[11:19]
    print(date1)
    print(time1)
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    cmod = Spec02.objects
    try:
        # data = cmod.filter(datetime__startswith=datetimequery[0:16]).values()
        data = cmod.filter(date=date1).filter(
            time__startswith=time1[0:5]).values()
        # filter(time__startswith=time).
        print(data)
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            #  json.dumps(your_data, default=str)
            # json_data = json.dumps(
            #     json_data, cls=DateEncoder, ensure_ascii=False)
            json_data = json.dumps(json_data, default=str)
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def showImageSpec02(request):
    datetimequery = request.GET['query']
    date = datetimequery[0:10]
    time = datetimequery[11:19]
    cmod = Spec02.objects
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    try:
        data = cmod.filter(date=date).filter(
            time__startswith=time[0:5]).values("wavelength", "reflectance")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            json_data = json.dumps(json_data, default=str)
            # print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
            # print(json_data)
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def findDataSpec03(request):
    datetimequery = request.GET['query']
    date1 = datetimequery[0:10]
    time1 = datetimequery[11:19]
    print(date1)
    print(time1)
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    cmod = Spec03.objects
    try:
        # data = cmod.filter(datetime__startswith=datetimequery[0:16]).values()
        data = cmod.filter(date=date1).filter(
            time__startswith=time1[0:5]).values()
        # filter(time__startswith=time).
        print(data)
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            #  json.dumps(your_data, default=str)
            # json_data = json.dumps(
            #     json_data, cls=DateEncoder, ensure_ascii=False)
            json_data = json.dumps(json_data, default=str)
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def showImageSpec03(request):
    datetimequery = request.GET['query']
    date = datetimequery[0:10]
    time = datetimequery[11:19]
    cmod = Spec03.objects
    if not datetimequery:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    try:
        data = cmod.filter(date=date).filter(
            time__startswith=time[0:5]).values("wavelength", "reflectance")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            json_data = json.dumps(json_data, default=str)
            # print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
            # print(json_data)
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def findDataPsrv1(request):
    date = request.GET['query']
    if not date:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    cmod = Psrv1.objects
    try:
        data = cmod.filter(date=date).values("date", "time", "nm_340", "nm_380", "nm_440", "nm_500",
                                             "nm_675", "nm_870", "nm_937", "nm_1020", "nm_1640", 'wktemp', "envitemp")
        # print(data)
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            json_data = json.dumps(json_data, default=str)
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def showImagePsrv1(request):
    date = request.GET['query']
    print(date)
    cmod = Psrv1.objects
    if not date:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    try:
        data = cmod.filter(date=date).values("date", "time", "nm_340", "nm_380", "nm_440", "nm_500",
                                             "nm_675", "nm_870", "nm_937", "nm_1020", "nm_1640", 'wktemp', "envitemp")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            json_data = json.dumps(json_data, default=str)
            # print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
            # print(json_data)
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def findprocessDataPsr(request):
    date = request.GET['query']
    if not date:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    cmod = Psrv2.objects
    try:
        data = cmod.filter(date=date).values("date", "time", "wZenith", "wAirmass", "wCloud", "wAOD340",
                                             "wAOD380", "wAOD440", "wAOD500", "wAOD675", "wAOD870", 'wAOD1020', "wAOD1640", "walpha", "wbeta", 'wAOD550', "wPW")
        # print(data)
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            json_data = json.dumps(json_data, default=str)
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)


def showprocessDataPsr(request):
    date = request.GET['query']
    print(date)
    cmod = Psrv2.objects
    if not date:
        responseDate = {'data': 0, 'code': '404', 'message': '请选择日期时间!'}
        return JsonResponse(responseDate)
    try:
        data = cmod.filter(date=date).values("date", "time", "wAOD550", "wPW")
        if data.count() == 0:
            responseDate = {'data': 0, 'code': '404', 'message': '沒有找到数据!'}
        else:
            json_data = list(data)
            json_data = json.dumps(json_data, default=str)
            # print(type(json_data))
            responseDate = {'data': json_data,
                            'code': '200', 'message': '获取成功!'}
            # print(json_data)
    except Exception as e:
        print("except:", e)
        print("未找到")
        responseDate = {'data': 0, 'code': '404', 'message': '错误!'}
    return JsonResponse(responseDate)
