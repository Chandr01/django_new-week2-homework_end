from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^results/(?P<a>\w+)&(?P<b>\w+)&(?P<c>\w+)$', views.results),

]