import logging

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from questions.models import Question

logger = logging.getLogger('django')

def index(request):
    questions = Question.objects.all()
    template = loader.get_template('questions/index.html')
    context = {
        'questions': questions
    }
    return HttpResponse(template.render(context, request))


def question_form(request):
    return render(request, 'questions/question_form.html')


def new_question(request):

    q = Question()
    q.question_title = request.POST['questionTitle']
    q.question_text = request.POST['questionText']

    q.save()

    return HttpResponseRedirect(reverse('questions:index'))
