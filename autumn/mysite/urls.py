"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = [
    url(r'^adautumnmin/', include(admin.site.urls)),
    url(r'^$', 'autumn.views.index', name='index'),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', 'autumn.views.blog', name='blog'),
    url(r'^author/(?P<author_id>[0-9]+)/$', 'autumn.views.author', name='author'),
    url(r'^register/$', 'autumn.views.register', name='register'),
    url(r'^login/$', 'autumn.views.login_view', name='login'),
    url(r'^logout/$', 'autumn.views.logout_view', name='logout_view'),
    url(r'^input/$', 'autumn.views.input', name='input'),
    url(r'^modify_blog/(?P<blog_id>[0-9]+)/$', 'autumn.views.modify_blog', name='modify_blog'),
    url(r'^about/$', 'autumn.views.about', name='about'),
    url(r'^comment/$', 'autumn.views.comment', name="comment"),
    url(r'^delete_blog/(?P<blog_id>[0-9]+)/$' , 'autumn.views.delete_blog', name="delete_blog"),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',),
    url(r'^staticfiles/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),
]
