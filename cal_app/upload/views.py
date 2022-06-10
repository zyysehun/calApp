import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from datetime import datetime

from upload.models import Cal
from upload.models import Cal02, Cal03, Calhim


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


def upload02(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    # print(content)
   #  print(type(content))
    length = len(content)
    cmod = Cal02.objects
    dstr = content[2]["1"]
    time = content[3]["1"]
    date = '-'.join([dstr[0:4], dstr[4:6], dstr[6:8]])
    datetimestr = date + '-'+time
    global datetime
    datetime = datetime.strptime(datetimestr, '%Y-%m-%d-%H:%M:%S')
    for key1 in content[8:]:

        try:

            ob = Cal02()
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


def upload03(request):
    body_unicode = request.body.decode()
    body = json.loads(body_unicode, strict=False)
    content = body['content']
    # print(content)
   #  print(type(content))
    length = len(content)
    cmod = Cal03.objects
    dstr = content[2]["1"]
    time = content[3]["1"]
    date = '-'.join([dstr[0:4], dstr[4:6], dstr[6:8]])
    datetimestr = date + '-'+time
    global datetime
    datetime = datetime.strptime(datetimestr, '%Y-%m-%d-%H:%M:%S')
    for key1 in content[8:]:

        try:

            ob = Cal03()
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
