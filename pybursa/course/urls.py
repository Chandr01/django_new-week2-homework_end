from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_),
    url(r'^course/(?P<identer>\d+)$', views.course_description),
    # url(r'^students/', views.students),
    url(r'^students/$', views.students),
    url(r'^student/(?P<id>\d+)$', views.student),
    url(r'^course/edit/(?P<pk>\d+)$', views.course_edit),
    url(r'^course/add$', views.course_add),
    url(r'^course/remove/(?P<pk>\d+)$', views.course_delete),
    url(r'^lesson/add/(?P<pk>\d+)$', views.lesson_add),

]
