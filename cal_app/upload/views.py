import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from datetime import datetime

from upload.models import Cal
from upload.models import Cal02, Cal03, Calhim, Spec01, Spec02, Spec03, Psrv1, Psrv2


"""
def upload(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    # print(content)
   #  print(type(content))
    length = len(content)
    cmod = Cal.objects
    dstr = content[2]["1"]
    time = content[3]["1"]
    date = '-'.join([dstr[0:4], dstr[4:6], dstr[6:8]])
    datetimestr = date + '-'+time
    global datetime
    datetime = datetime.strptime(datetimestr, '%Y-%m-%d-%H:%M:%S')
    for key1 in content[8:]:

        try:

            ob = Cal()
            ob.datetime = datetime
            for key in key1:
                ob.wavelength = key1["0"]
                ob.caldata = key1["1"]
                ob.save()
        except Exception as err:
            print(err)
    # 将data放入字典中
    data = {'data': length, 'code': '200', 'message': '获取成功!'}
    # 返回前端json

#    date = content[2][0]
#    time = content[3][0]
#    for key1 in content[8:]:
#        for key in key1:
#            print(key1[key],end = ' ')
    #    print()
    return JsonResponse(data=data, safe=False)
    
    def uploadSpec01(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    # print(content)
    length = len(content)
    dstr = content[2]["1"]
    time = content[3]["1"]
    date = '-'.join([dstr[0:4], dstr[4:6], dstr[6:8]])
    datetimestr = date + '-'+time
    print(datetimestr)
    global datetime
    datetime = datetime.strptime(datetimestr, '%Y-%m-%d-%H:%M:%S')
    data = {}
    isExistDatetime = Spec01.objects.filter(datetime=datetime)
    if isExistDatetime:
        data = {'data': length, 'code': '400', 'message': '数据已经存在!'}
        return JsonResponse(data=data, safe=False)
    #     # 将data放入字典中
    for key1 in content[6:1207]:
        try:
            ob = Spec01()
            ob.datetime = datetime
            for key in key1:
                ob.wavelength = key1["0"]
                ob.reflectance = key1["1"]
                ob.save()
                data = {'data': length, 'code': '200', 'message': '数据上传成功!'}
        except Exception as err:
            print("except:", err)
            data = {'data': length, 'code': '400', 'message': '数据上传失败!'}
    return JsonResponse(data=data, safe=False)
"""


def upload(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    length = len(content)
    cmod = Cal.objects
    date = content[2]["1"]
    time = content[3]["1"]
    print(date)
    print(time)
    date = '-'.join([date[0:4], date[4:6], date[6:8]])
    data = {}
    isExistDatetime = Cal.objects.filter(date=date).filter(
        time__startswith=time[0:5])
    if isExistDatetime:
        data = {'data': length, 'code': '400', 'message': '数据已经存在!'}
        return JsonResponse(data=data, safe=False)
    #     # 将data放入字典中
    for key1 in content[8:length-1]:
        try:
            ob = Cal()
            ob.date = date
            ob.time = time
            for key in key1:
                ob.wavelength = key1["0"]
                ob.caldata = key1["1"]
                ob.save()
                data = {'data': length, 'code': '200', 'message': '数据上传成功!'}
        except Exception as err:
            print("except:", err)
            data = {'data': length, 'code': '400', 'message': '数据上传失败!'}
    return JsonResponse(data=data, safe=False)


def upload02(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    length = len(content)
    cmod = Cal02.objects
    date = content[2]["1"]
    time = content[3]["1"]
    print(date)
    print(time)
    date = '-'.join([date[0:4], date[4:6], date[6:8]])
    data = {}
    isExistDatetime = Cal02.objects.filter(date=date).filter(
        time__startswith=time[0:5])
    if isExistDatetime:
        data = {'data': length, 'code': '400', 'message': '数据已经存在!'}
        return JsonResponse(data=data, safe=False)
    #     # 将data放入字典中
    for key1 in content[8:length-1]:
        try:
            ob = Cal02()
            ob.date = date
            ob.time = time
            for key in key1:
                ob.wavelength = key1["0"]
                ob.caldata = key1["1"]
                ob.save()
                data = {'data': length, 'code': '200', 'message': '数据上传成功!'}
        except Exception as err:
            print("except:", err)
            data = {'data': length, 'code': '400', 'message': '数据上传失败!'}
    return JsonResponse(data=data, safe=False)


def upload03(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    length = len(content)
    cmod = Cal03.objects
    date = content[2]["1"]
    time = content[3]["1"]
    print(date)
    print(time)
    date = '-'.join([date[0:4], date[4:6], date[6:8]])
    data = {}
    isExistDatetime = Cal03.objects.filter(date=date).filter(
        time__startswith=time[0:5])
    if isExistDatetime:
        data = {'data': length, 'code': '400', 'message': '数据已经存在!'}
        return JsonResponse(data=data, safe=False)
    #     # 将data放入字典中
    for key1 in content[8:length-1]:
        try:
            ob = Cal03()
            ob.date = date
            ob.time = time
            for key in key1:
                ob.wavelength = key1["0"]
                ob.caldata = key1["1"]
                ob.save()
                data = {'data': length, 'code': '200', 'message': '数据上传成功!'}
        except Exception as err:
            print("except:", err)
            data = {'data': length, 'code': '400', 'message': '数据上传失败!'}
    return JsonResponse(data=data, safe=False)


def uploadHIM(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    length = len(content)
    cmod = Calhim.objects
    date = content[2]["1"]
    time = content[3]["1"]
    print(date)
    print(time)
    date = '-'.join([date[0:4], date[4:6], date[6:8]])
    data = {}
    isExistDatetime = Calhim.objects.filter(date=date).filter(
        time__startswith=time[0:5])
    if isExistDatetime:
        data = {'data': length, 'code': '400', 'message': '数据已经存在!'}
        return JsonResponse(data=data, safe=False)
    #     # 将data放入字典中
    for key1 in content[8:length-1]:
        try:
            ob = Calhim()
            ob.date = date
            ob.time = time
            for key in key1:
                ob.wavelength = key1["0"]
                ob.diff = key1["1"]
                ob.global_irr = key1["2"]
                ob.direct = key1["3"]
                ob.dg_radio = key1["4"]
                ob.save()
                data = {'data': length, 'code': '200', 'message': '数据上传成功!'}
        except Exception as err:
            print("except:", err)
            data = {'data': length, 'code': '400', 'message': '数据上传失败!'}
    return JsonResponse(data=data, safe=False)


def uploadSpec01(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    length = len(content)
    cmod = Spec01.objects
    date = content[2]["1"]
    time = content[3]["1"]
    print(date)
    print(time)
    date = '-'.join([date[0:4], date[4:6], date[6:8]])
    data = {}
    isExistDatetime = Spec01.objects.filter(date=date).filter(
        time__startswith=time[0:5])
    if isExistDatetime:
        data = {'data': length, 'code': '400', 'message': '数据已经存在!'}
        return JsonResponse(data=data, safe=False)
    #     # 将data放入字典中
    for key1 in content[6:length-1]:
        try:
            ob = Spec01()
            ob.date = date
            ob.time = time
            for key in key1:
                ob.wavelength = key1["0"]
                ob.reflectance = key1["1"]
                ob.save()
                data = {'data': length, 'code': '200', 'message': '数据上传成功!'}
        except Exception as err:
            print("except:", err)
            data = {'data': length, 'code': '400', 'message': '数据上传失败!'}
    return JsonResponse(data=data, safe=False)


def uploadSpec02(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    length = len(content)
    cmod = Spec02.objects
    date = content[2]["1"]
    time = content[3]["1"]
    print(date)
    print(time)
    date = '-'.join([date[0:4], date[4:6], date[6:8]])
    data = {}
    isExistDatetime = Spec02.objects.filter(date=date).filter(
        time__startswith=time[0:5])
    if isExistDatetime:
        data = {'data': length, 'code': '400', 'message': '数据已经存在!'}
        return JsonResponse(data=data, safe=False)
    #     # 将data放入字典中
    for key1 in content[6:length-1]:
        try:
            ob = Spec02()
            ob.date = date
            ob.time = time
            for key in key1:
                ob.wavelength = key1["0"]
                ob.reflectance = key1["1"]
                ob.save()
                data = {'data': length, 'code': '200', 'message': '数据上传成功!'}
        except Exception as err:
            print("except:", err)
            data = {'data': length, 'code': '400', 'message': '数据上传失败!'}
    return JsonResponse(data=data, safe=False)


def uploadSpec03(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    length = len(content)
    cmod = Spec03.objects
    date = content[2]["1"]
    time = content[3]["1"]
    print(date)
    print(time)
    date = '-'.join([date[0:4], date[4:6], date[6:8]])
    data = {}
    isExistDatetime = Spec03.objects.filter(date=date).filter(
        time__startswith=time[0:5])
    if isExistDatetime:
        data = {'data': length, 'code': '400', 'message': '数据已经存在!'}
        return JsonResponse(data=data, safe=False)
    #     # 将data放入字典中
    for key1 in content[6:length-1]:
        try:
            ob = Spec03()
            ob.date = date
            ob.time = time
            for key in key1:
                ob.wavelength = key1["0"]
                ob.reflectance = key1["1"]
                ob.save()
                data = {'data': length, 'code': '200', 'message': '数据上传成功!'}
        except Exception as err:
            print("except:", err)
            data = {'data': length, 'code': '400', 'message': '数据上传失败!'}
    return JsonResponse(data=data, safe=False)


"""def uploadSpec03(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    # print(content)
    length = len(content)
    dstr = content[2]["1"]
    time = content[3]["1"]
    date = '-'.join([dstr[0:4], dstr[4:6], dstr[6:8]])
    datetimestr = date + '-'+time
    global datetime
    datetime = datetime.strptime(datetimestr, '%Y-%m-%d-%H:%M:%S')
    data = {}
    isExistDatetime = Spec03.objects.filter(datetime=datetime)
    if isExistDatetime:
        data = {'data': length, 'code': '400', 'message': '数据已经存在!'}
        return JsonResponse(data=data, safe=False)
    #     # 将data放入字典中
    for key1 in content[6:1207]:
        try:
            ob = Spec03()
            ob.datetime = datetime
            for key in key1:
                ob.wavelength = key1["0"]
                ob.reflectance = key1["1"]
                ob.save()
                data = {'data': length, 'code': '200', 'message': '数据上传成功!'}
        except Exception as err:
            print("except:", err)
            data = {'data': length, 'code': '400', 'message': '数据上传失败!'}
    return JsonResponse(data=data, safe=False)
"""


def uploadPsrv1(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    length = len(content)
    cmod = Psrv1.objects
    date = content[1]["1"]
    # print(date)
    date = '-'.join([date[0:4], date[5:7], date[8:10]])
    print(date)
    data = {}
    isExistDatetime = Psrv1.objects.filter(date=date)
    if isExistDatetime:
        data = {'data': length, 'code': '400', 'message': '数据已经存在!'}
        return JsonResponse(data=data, safe=False)
    #     # 将data放入字典中
    for key1 in content[1:length-1]:
        try:
            ob = Psrv1()
            ob.date = date
            for key in key1:
                ob.time = key1["2"]
                ob.nm_340 = key1["3"]
                ob.nm_380 = key1["4"]
                ob.nm_440 = key1["5"]
                ob.nm_500 = key1["6"]
                ob.nm_675 = key1["7"]
                ob.nm_870 = key1["8"]
                ob.nm_937 = key1["9"]
                ob.nm_1020 = key1["10"]
                ob.nm_1640 = key1["11"]
                ob.wktemp = key1["12"]
                ob.envitemp = key1["13"]
                ob.envihumi = key1["14"]
                ob.pressure = key1["15"]
                ob.Inenvitemp = key1["16"]
                ob.Inenvihumi = key1["17"]
                ob.Headtemp = key1["18"]
                ob.Headhumi = key1["19"]
                ob.FQ1 = key1["20"]
                ob.FQ2 = key1["21"]
                ob.FQ3 = key1["22"]
                ob.FQ4 = key1["23"]
                ob.save()
                data = {'data': length, 'code': '200', 'message': '数据上传成功!'}
        except Exception as err:
            print("except:", err)
            data = {'data': length, 'code': '400', 'message': '数据上传失败!'}
    return JsonResponse(data=data, safe=False)


def processDataPsr(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    length = len(content)
    cmod = Psrv2.objects
    date = content[1]["1"]
    # print(date)
    date = '-'.join([date[0:4], date[5:7], date[8:10]])
    data = {}
    isExistDatetime = Psrv2.objects.filter(date=date)
    if isExistDatetime:
        data = {'data': length, 'code': '400', 'message': '数据已经存在!'}
        return JsonResponse(data=data, safe=False)
    #     # 将data放入字典中
    for key1 in content[1:length-1]:
        try:
            ob = Psrv2()
            ob.date = date
            for key in key1:
                ob.time = key1["2"]
                ob.wZenith = key1["3"]
                ob.wAirmass = key1["4"]
                ob.wCloud = key1["5"]
                ob.wAOD340 = key1["6"]
                ob.wAOD380 = key1["7"]
                ob.wAOD440 = key1["8"]
                ob.wAOD500 = key1["9"]
                ob.wAOD675 = key1["10"]
                ob.wAOD870 = key1["11"]
                ob.wAOD1020 = key1["12"]
                ob.wAOD1640 = key1["13"]
                ob.walpha = key1["14"]
                ob.wbeta = key1["15"]
                ob.wAOD550 = key1["16"]
                ob.wPW = key1["17"]

                ob.save()
                data = {'data': length, 'code': '200', 'message': '数据上传成功!'}
        except Exception as err:
            print("except:", err)
            data = {'data': length, 'code': '400', 'message': '数据上传失败!'}
    return JsonResponse(data=data, safe=False)
