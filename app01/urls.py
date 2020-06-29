from django.conf.urls import url,include
from app01 import views
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    url(r'^equipinfo/', views.equipinfo),
    url(r'^equipadd/', views.equipadd),
    url(r'^equipmaintain/', views.equipmaintain),
    url(r'^equipallot/', views.equipallot),
    url(r'^euipscrap/', views.euipscrap),
    url(r'^supplerinfo/', views.supplerinfo),
    url(r'^suppleradd/', views.suppleradd),
    url(r'^contractlist/', views.contractlist),
    url(r'^constractadd/', views.constractadd),
    url(r'^contractclass/', views.contractclass),
    url(r'^maintaininfo/', views.maintaininfo),

    url(r'^media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT})
    ]