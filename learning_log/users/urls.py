"""为应用程序users定义URL模式"""
from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    #登录页面
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    #登出
    url(r'^logout/$', views.logout_view, name='logout'),
    #注册页面
    url(r'^register/$', views.register, name='register'),
]
