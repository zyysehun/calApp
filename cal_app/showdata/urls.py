from django.urls import path
from . import views

urlpatterns = [
    path('finddata/', views.findData),
    path('showimage/', views.showImage),
    path('finddata02/', views.findData02),
    path('showimage02/', views.showImage02),
    path('finddata03/', views.findData03),
    path('showimage03/', views.showImage03),
]
