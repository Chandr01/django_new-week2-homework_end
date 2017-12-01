from django import forms
from course.models import Course, Lesson, Tester, Students


class ModelCourseEditForm(forms.ModelForm):
    fields = ['short_description']

    class Meta:
        model = Course

        exclude = []
        # widgets = {'packag': forms.RadioSelect}
        # labels = {'email': 'Mail'}


class ModelLessonEditForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ['order']


class ModelStudentsEditForm(forms.ModelForm):
    class Meta:
        model = Students
        exclude = ['']
