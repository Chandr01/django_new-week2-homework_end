from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    response = HttpResponse("Index page")
    return response


def results(request):
    # resp = "a = {} b = {} c = {}".format(a, b, c)
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    aa = False
    try:
        a = int(a)
        b = int(b)
        c = int(c)

    except:
        aa = True

    if aa == True:
        resp = "a = {} b = {} c = {}, koefficient ne opredelen".format(a, b, c)
    elif int(a) == 0:
        resp = "a = {} b = {} c = {}, a nt mozhet bit ravno 0".format(a, b, c)
        print(2)
    else:
        resp = int(a) + int(b) + int(c)
        print(4)
    # response = HttpResponse(resp)
    # return response
    return render(request, 'result.html', {'resp': resp,
                                           'a': a,
                                           'b': b,
                                           "c": c}, )
