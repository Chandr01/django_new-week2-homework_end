from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    response = HttpResponse("Index page")
    return response


from django import forms


class QuadricForms(forms.Form):
    a = forms.CharField(max_length=100)
    b = forms.CharField(max_length=100)
    c = forms.CharField(max_length=100)


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
