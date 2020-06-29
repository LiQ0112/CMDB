"""CMDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from app01 import views
from app01 import urls as app_url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^reg/', views.reg),
    url(r'^logout/', views.logout),
    url('check_user/', views.check_user),
    url(r'^index/$', views.index),
    url(r'^index/', include(app_url)),
    url(r'^$', views.login),
    url(r'^classadd/$', views.classadd),
    # url(r'^base1/$', views.base1),
    url(r'^mi/$', views.mi),
    url(r'^reset_password/$', views.reset_password),
    #合同下载
    url(r'^contract_download/(\d+)$', views.contract_download),
    url(r'^check_password/(\d+)$', views.check_password),

    url(r'^media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT})
]
