from django.shortcuts import render
from course.models import Course, Lesson, Students


# Create your views here.
def course_(request):
    course = Course.objects.all()

    return render(request, 'course/index.html', {'course': course})


def course_description(request, identer):
    course = Course.objects.get(id=identer)
    lessons = Lesson.objects.filter(course=course)

    return render(request, 'course/details.html', {'course': course,
                                           'lessons': lessons})


def students(request):
    page_num = request.GET.get('id', 0)
    if page_num == 0:
        students = Students.objects.all()
        return render(request, 'students/student.html', {'students': students})
    else:
        students = Students.objects.filter(courses=page_num)
        return render(request, 'students/student.html', {'students': students})


def student(request, id):
    student = Students.objects.get(id=id)
    return render(request, 'students/index.html', {'student': student})
