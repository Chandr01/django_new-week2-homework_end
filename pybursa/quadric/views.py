from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from quadric.models import Quadric_logik
from django.contrib import messages


# Create your views here.

def index(request):
    response = HttpResponse("Index page")
    return response


from django import forms


class QuadricForms(forms.Form):
    a = forms.CharField(max_length=100)
    b = forms.CharField(max_length=100)
    c = forms.CharField(max_length=100)


class CorseApplyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(label='Mail', required=False)
    packag = forms.ChoiceField(choices=(('standart', 'Standart'),
                                        ('gold', 'Gold'),
                                        ('vip', 'VIP')), widget=forms.RadioSelect)
    name_subscribe = forms.BooleanField(help_text='Hello Chan')


class ModelCourseApplyForm(forms.ModelForm):
    class Meta:
        model = Quadric_logik
        exclude = ['date_apply', 'is_active', 'comment']
        widgets = {'packag': forms.RadioSelect}
        labels = {'email': 'Mail'}


def apply_delete(request, pk):
    # print(pk)
    quadric_logik = Quadric_logik.objects.get(id=pk)
    form = ModelCourseApplyForm(instance=quadric_logik)
    if request.method == 'POST':
        quadric_logik.delete()

        messages.success(request, 'Deleted')
        return redirect('/quadric/apply/')
    else:
        form = ModelCourseApplyForm(instance=quadric_logik)
    return render(request, 'result_delete.html', {'quadric_logik': quadric_logik})


def apply_edit(request, pk):
    # print(pk)
    quadric_logik = Quadric_logik.objects.get(id=pk)
    form = ModelCourseApplyForm(instance=quadric_logik)
    if request.method == 'POST':
        form = ModelCourseApplyForm(request.POST, instance=quadric_logik)
        if form.is_valid():
            quadric_logik = form.save()

            messages.success(request, 'Saved')
            return redirect('/quadric/apply/')
    else:
        form = ModelCourseApplyForm(instance=quadric_logik)
    return render(request, 'result_edit.html', {'form': form})


def apply(request):
    # model_form = ModelCourseApplyForm()
    if request.method == 'POST':
        form = ModelCourseApplyForm(request.POST)
        if form.is_valid():
            instance = form.save()

            messages.success(request, 'Saved')
            return redirect('/quadric/apply/')
    else:
        form = ModelCourseApplyForm(initial={'packag': 'gold',
                                             'name_subscribe': True})
    # form = CorseApplyForm()
    return render(request, 'result.html', {'form': form})


def results(request):
    form = QuadricForms()
    print(request.GET.get('a'))
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    resp = "a = {} b = {} c = {}".format(a, b, c)

    # resp['form'] = form
    def tryse(z):
        try:
            z = int(z)
            return z
        except:
            z = 'error'
            return z

    a = tryse(a)
    b = tryse(b)
    c = tryse(c)
    errors = {
        'a_error': False,
        'b_error': False,
        'c_error': False
    }
    if a == 'error':
        errors['a_error'] = 'Error'
    if b == 'error':
        errors['b_error'] = 'Error'
    if c == 'error':
        errors['c_error'] = 'Error'

    if a != 'error' and b != 'error' and c != 'error' and a != 0:
        resp = int(a) ** 2 + int(b) + int(c)
    elif a == 0:
        resp = 'a - Ne mozet bit nulem'
    else:
        resp = 'Oshibka Argumetna'
    return render(request, 'result.html', {'resp': resp,
                                           'a': a,
                                           'b': b,
                                           'c': c,
                                           'a_error': errors['a_error'],
                                           'b_error': errors['b_error'],
                                           'c_error': errors['c_error'],
                                           'form': form}, )
