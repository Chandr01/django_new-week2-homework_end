
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.course_),
    url(r'^course/(?P<identer>\d+)$', views.course_description),
    # url(r'^students/', views.students),
    url(r'^students/$', views.students),
    url(r'^student/(?P<id>\d+)$', views.student),

    ]