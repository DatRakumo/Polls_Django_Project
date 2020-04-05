# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


# Create your views here.

def index(request):
    name = "NGuyen Van Dat "
    taisan = {"DIen thoai", "Laptop", "Xe may"}
    context = {"name": name, "taisan": taisan}
    return render(request, "polls/index.html", context)


""" 
def showDetail(request, pk):
    #q = get_object_or_404(Question, pk=pk)
    q = Question.objects.get(pk = pk)
    if q:
        context = {"item": q }
        return render(request, "polls/question_detail.html", context)
        # return HttpResponse("You're looking at question %s." % context)
    else:
        context = {"item": "Khong tim thay"}
        return HttpResponse("You're looking at question %s." % context)

    # return render(request, "polls/question_detail.html", context)
    
"""


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def showList(request):
    questions = Question.objects.all()
    # questions = get_object_or_404(Question, pk = 2)
    context = {"questions": questions}

    return render(request, "polls/question_list.html", context)
