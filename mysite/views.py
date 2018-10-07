from django.http import HttpResponse, Http404
from datetime import datetime, timedelta
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse('Hello World!')


def current_datetime(request):
    current_date = datetime.now()
    name = 'magistr'

    # locals() - вернет словарь всех локальных переменных
    return render_to_response('current_datetime.html', locals())

def mypage(request):
    return render_to_response('mypage.html',{'current_section': str(request), 'title': 'HOME_PROJECT'})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now_offset = datetime.now() + timedelta(hours=offset)
    return render_to_response('hours_ahead.html',{'now_offset': now_offset, 'offset': offset})
