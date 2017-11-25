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


def apply(request):
    if request.method == 'POST':
        form = CorseApplyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            course_apply = Quadric_logik()
            course_apply.name = data['name']
            course_apply.email = data['email']
            course_apply.packag = data['packag']
            course_apply.name_subscribe = data['name_subscribe']
            course_apply.save()
            messages.success(request, 'Saved')
            return redirect('/quadric/apply/')
    else:
        form = CorseApplyForm(initial={'packag': 'gold',
                                       'name_subscribe': True})
    # form = CorseApplyForm()
    return render(request, 'apply.html', {'form': form})


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
