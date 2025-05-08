#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：my_blog 
@File    ：urls.py.py
@IDE     ：PyCharm 
@Author  ：RyougiShiki
@Date    ：2025/5/8 下午7:52 
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]