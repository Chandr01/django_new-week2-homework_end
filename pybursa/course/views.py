from django.shortcuts import render
from course.models import Course, Lesson, Students
from course.forms import ModelCourseEditForm, ModelLessonEditForm, ModelStudentsEditForm
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


# Create your views here.
class TopCourseMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.all()[:5]
        return context


class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Students
    # form_class = ModelStudentsEditForm
    success_url = reverse_lazy('list')
    template_name = 'student_delete.html'
    # context_object_name = 'form'
    success_message = "Student %(name)s was removed successfully"
    context_object_name = 'form'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)


class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Students
    form_class = ModelStudentsEditForm
    success_url = reverse_lazy('list')
    template_name = 'student_edit.html'
    context_object_name = 'form'
    success_message = 'Data Updated'

    def from_valid(self, form):
        response = super().form_valid(form)
        student = form.save()
        return response


class StudentCreateView(SuccessMessageMixin, CreateView):
    form_class = ModelStudentsEditForm
    success_url = '/students'
    template_name = 'student_add.html'
    context_object_name = 'form'
    success_message = '%(name) Created'

    def from_valid(self, form):
        response = super().form_valid(form)
        student = form.save()
        return response


class SomeFormView(FormView):
    form_class = ModelStudentsEditForm
    context_object_name = 'form'
    initial = {}

    template_name = 'student_edit.html'
    success_url = 'students/'

    def from_valid(self, form):
        student = form.save()
        messages.success(self.request, 'Data changed')


class StudentListView(ListView):
    model = Students
    template_name = 'students.html'
    context_object_name = 'students'
    initial = {}

    def get_queryset(self):
        qs = super().get_queryset()
        page_num = self.request.GET.get('course_id', None)
        if page_num:
            qs = qs.filter(courses__id=page_num)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Student - pyBursa'
        return context


class StudentDetailView(DetailView):
    model = Students
    template_name = 'student.html'


class IndexView(TopCourseMixin, TemplateView):
    template_name = 'index.html'


def course_(request):
    course = Course.objects.all()

    return render(request, 'index.html', {'course': course})


def course_description(request, identer):
    course = Course.objects.get(id=identer)
    lessons = Lesson.objects.filter(course=course)

    return render(request, 'course_detail.html', {'course': course,
                                                  'lessons': lessons})


# def students(request):
#     page_num = request.GET.get('id', 0)
#     if page_num == 0:
#         students = Students.objects.all()
#         return render(request, 'students.html', {'students': students})
#     else:
#         students = Students.objects.filter(courses=page_num)
#         return render(request, 'students.html', {'students': students})
#
#
# def student(request, id):
#     student = Students.objects.get(id=id)
#     return render(request, 'student.html', {'student': student})


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
        form = ModelLessonEditForm(initial={'course': course})
    # form = CorseApplyForm()
    return render(request, 'lesson_add.html', {'form': form})

# def students_add(request):
#     # model_form = ModelCourseApplyForm()
#     if request.method == 'POST':
#         form = ModelStudentsEditForm(request.POST)
#         if form.is_valid():
#             instance = form.save()
#             # print(instance)
#             messages.success(request, 'Student {} was added'.format(instance))
#             return redirect('/students')
#     else:
#         form = ModelStudentsEditForm()
#         # print('No instance')
#     # form = CorseApplyForm()
#     return render(request, 'student_add.html', {'form': form})
#
#
# def student_delete(request, pk):
#     # print(pk)
#     delete_form = Students.objects.get(id=pk)
#     print(delete_form)
#     # print('Тип формы', type(modelcoursedeleteform['name']))
#     form = ModelStudentsEditForm(instance=delete_form)
#     if request.method == 'POST':
#         delete_form.delete()
#
#         messages.success(request, 'Student {} deleted'.format(delete_form))
#         return redirect('/students')
#     else:
#         form = ModelStudentsEditForm(instance=delete_form)
#     return render(request, 'student_delete.html', {'delete_form': delete_form})

# def student_edit(request, pk):
#     # print(pk)
#     edit_form = Students.objects.get(id=pk)
#     form = ModelStudentsEditForm(instance=edit_form)
#     if request.method == 'POST':
#         form = ModelStudentsEditForm(request.POST, instance=edit_form)
#         if form.is_valid():
#             edit_form = form.save()
#
#             messages.success(request, 'Изменения в курсе {} сохранены'.format(edit_form))
#             return redirect('/students')
#     else:
#         form = ModelStudentsEditForm(instance=edit_form)
#     return render(request, 'student_edit.html', {'edit_form': form})
