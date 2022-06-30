from django.urls import path
from . import views

urlpatterns = [
    path('compute6S/', views.compute6S, name='compute6S'),

]
