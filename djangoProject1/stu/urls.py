"""
@project:djangoProject1
@author:zlh
@file:urls.py
@time:2021/1/25 21:52
"""
#coding=utf-8
from django.urls import include,path
from . import views
urlpatterns={
    path('',views.index_view),
    path('login/',views.login_view),
}