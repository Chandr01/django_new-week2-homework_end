from django.shortcuts import render
from course.models import Course


# Create your views here.
def course_(request):
    course = Course.objects.get()

    return render(request, 'course.html', {'course': course,
                                           'name': course.name,
                                           'field': course.short_description,
                                           'text_field': course.description})
