from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from questions.models import Question


def index(request):
    questions = Question.objects.all()
    template = loader.get_template('questions/index.html')
    context = {
        'questions' : questions
    }
    return HttpResponse(template.render(context, request))

def question_form(request):
    template = loader.get_template('questions/question_form.html')
    return HttpResponse(template.render(request))