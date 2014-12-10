from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cloudinary_example.core.views',
    url(r'^galeria/$', 'galeria', name='galeria'),
)