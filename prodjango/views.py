from django.http import HttpResponse

def first(request):
    l = [1,2,3,4,5,6]

    return HttpResponse(f"{l}")
def second(request):
    return HttpResponse("<h>Hello world</h1>")