from django.http import HttpResponse


def helloworldfunc(request):
    responseobject = HttpResponse('<h1>helloworld</h1>')
    return responseobject

def hatoyafunc(request):
    responseobject = HttpResponse('<h2>helloopen</h2>')
    return responseobject

def partfunc(request):
    responseobject = HttpResponse('<h4>課題</h4>')
    return responseobject

def songfunc(request):
    responseobject = HttpResponse('<h10>GIT</h10>')
    return responseobject

def showfunc(request):
    responseobject = HttpResponse('<h2 style="color:blue">暑中お見舞い申し上げます</h10>')
    return responseobject