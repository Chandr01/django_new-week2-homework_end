from django.contrib import admin
from course.models import Course, Students, Lesson


# Register your models here.

# class CourseAdmin(admin.ModelAdmin):
#     def get_name(self, obj):
#         return obj.user.first_name


admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Students)
