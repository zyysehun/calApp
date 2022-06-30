from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('upload02/', views.upload02, name='upload02'),
    path('upload03/', views.upload03, name='upload03'),
    path('uploadhim/', views.uploadHIM, name='uploadHIM'),
    path('uploadspec01/', views.uploadSpec01, name='uploadSpec01'),
    path('uploadspec02/', views.uploadSpec02, name='uploadSpec02'),
    path('uploadspec03/', views.uploadSpec03, name='uploadSpec03'),
    path('uploadpsrv1/', views.uploadPsrv1, name='uploadPsrv1'),
    path('processDataPsr/', views.processDataPsr),
    # path('check/', views.check, name='check'),
    # path('api/hellopostjson', views.HelloPostJson),
    # path('login', views.login),
]
