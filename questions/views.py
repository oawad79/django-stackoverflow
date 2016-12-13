from django.http import HttpResponse
import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.template import loader
from django.template.context_processors import csrf
from django.urls import reverse

from questions.models import Question


logger = logging.getLogger('django')

def index(request):
    questions = Question.objects.all()
    template = loader.get_template('questions/index.html')
    context = {
        'questions' : questions
    }
    return HttpResponse(template.render(context, request))

def question_form(request):
    #template = loader.get_template('questions/question_form.html')
    context = {'foo': 'bar'}
    return render(request, 'questions/question_form.html', context)

def new_question(request):

    logger.debug('request = **************************************')
    logger.info("testing")

    questions = Question.objects.all()
    template = loader.get_template('questions/index.html')
    context = {
        'questions': questions
    }
    return render(request, 'questions/index.html', context)