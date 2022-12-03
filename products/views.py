from django.shortcuts import HttpResponse
import datetime

def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_data(request):
    if request.method == 'GET':
        date = datetime.datetime.now().date()
        return HttpResponse(date)


def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')


