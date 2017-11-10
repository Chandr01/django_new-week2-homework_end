from django.contrib import admin
from course.models import Course, Students, Lesson

# Register your models here.


admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Students)
