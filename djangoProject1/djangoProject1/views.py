"""
@project:DjangoTest1
@author:zlh
@file:views.py
@time:2021/1/25 16:29
"""
#encoding = utf=8

#显示hello
from django.http import HttpResponse


def index_view():

    return HttpResponse("hello world")