from django.urls import path
from . import views

urlpatterns = [
    path('finddata/', views.findData),
    path('showimage/', views.showImage),
    path('finddata02/', views.findData02),
    path('showimage02/', views.showImage02),
    path('finddata03/', views.findData03),
    path('showimage03/', views.showImage03),
    path('finddatahim/', views.findDataHIM),
    path('showimagehim/', views.showImageHIM),
    path('finddataspec01/', views.findDataSpec01),
    path('showimagespec01/', views.showImageSpec01),
    path('finddataspec02/', views.findDataSpec02),
    path('showimagespec02/', views.showImageSpec02),
    path('finddataspec03/', views.findDataSpec03),
    path('showimagespec03/', views.showImageSpec03),
    path('finddatapsrv1/', views.findDataPsrv1),
    path('showimagepsrv1/', views.showImagePsrv1),
    path('findprocessDataPsr/', views.findprocessDataPsr),
    path('showprocessDataPsr/', views.showprocessDataPsr),
]
