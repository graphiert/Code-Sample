from django.shortcuts import render
from django.http import HttpResponse

def useRender(request):
    return render(request, 'index.html')

def useHttpResponse(request):
    return HttpResponse("Response ini dibuat dengan HttpResponse")
