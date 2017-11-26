from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^results/$', views.results),
    url(r'^apply/$', views.apply),
    url(r'^apply/(?P<pk>\d+)/edit/$', views.apply_edit),
    url(r'^apply/(?P<pk>\d+)/delete/$', views.apply_delete),


]