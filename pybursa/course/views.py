from django.shortcuts import render
from course.models import Course, Lesson, Students
from course.forms import ModelCourseEditForm, ModelLessonEditForm
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def course_(request):
    course = Course.objects.all()

    return render(request, 'index.html', {'course': course})


def course_description(request, identer):
    course = Course.objects.get(id=identer)
    lessons = Lesson.objects.filter(course=course)

    return render(request, 'course_detail.html', {'course': course,
                                                  'lessons': lessons})


def students(request):
    page_num = request.GET.get('id', 0)
    if page_num == 0:
        students = Students.objects.all()
        return render(request, 'students.html', {'students': students})
    else:
        students = Students.objects.filter(courses=page_num)
        return render(request, 'students.html', {'students': students})


def student(request, id):
    student = Students.objects.get(id=id)
    return render(request, 'student.html', {'student': student})


def course_add(request):
    # model_form = ModelCourseApplyForm()
    if request.method == 'POST':
        form = ModelCourseEditForm(request.POST)
        if form.is_valid():
            instance = form.save()
            # print(instance)
            messages.success(request, 'Курс {} был создан'.format(instance))
            return redirect('/')
    else:
        form = ModelCourseEditForm()
    # form = CorseApplyForm()
    return render(request, 'course_add.html', {'form': form})


def course_delete(request, pk):
    # print(pk)
    modelcoursedeleteform = Course.objects.get(id=pk)
    # print('Тип формы', type(modelcoursedeleteform['name']))
    form = ModelCourseEditForm(instance=modelcoursedeleteform)
    if request.method == 'POST':
        modelcoursedeleteform.delete()

        messages.success(request, 'Курс {} удален'.format(modelcoursedeleteform))
        return redirect('/')
    else:
        form = ModelCourseEditForm(instance=modelcoursedeleteform)
    return render(request, 'course_delete.html', {'modelcoursedeleteform': modelcoursedeleteform})


def course_edit(request, pk):
    # print(pk)
    modelcourseeditform = Course.objects.get(id=pk)
    form = ModelCourseEditForm(instance=modelcourseeditform)
    if request.method == 'POST':
        form = ModelCourseEditForm(request.POST, instance=modelcourseeditform)
        if form.is_valid():
            modelcourseeditform = form.save()

            messages.success(request, 'Изменения в курсе {} сохранены'.format(modelcourseeditform))
            return redirect('/')
    else:
        form = ModelCourseEditForm(instance=modelcourseeditform)
    return render(request, 'course_edit.html', {'modelcourseeditform': form})


def lesson_add(request, pk):
    # model_form = ModelCourseApplyForm()
    course = Course.objects.get(id=pk)
    print(pk, course)
    if request.method == 'POST':
        form = ModelLessonEditForm(request.POST)
        if form.is_valid():
            instance = form.save()
            # print(instance)
            messages.success(request, 'Урок {} был доавлен'.format(instance))
            return redirect('/course/{}'.format(pk))
    else:
        form =  ModelLessonEditForm(initial={'course': course})
    # form = CorseApplyForm()
    return render(request, 'lesson_add.html', {'form': form})
