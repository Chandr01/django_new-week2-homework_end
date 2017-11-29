from django import forms
from course.models import Course, Lesson, Tester


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
