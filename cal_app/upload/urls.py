from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('upload02/', views.upload02, name='upload02'),
    path('upload03/', views.upload03, name='upload03'),
    # path('check/', views.check, name='check'),
    # path('api/hellopostjson', views.HelloPostJson),
    # path('login', views.login),
]
