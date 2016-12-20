import logging

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from questions.models import Question, Category

logger = logging.getLogger('django')


def index(request):
    questions = Question.objects.all()
    template = loader.get_template('questions/index.html')
    context = {
        'questions': questions
    }
    return HttpResponse(template.render(context, request))


def question_form(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'questions/question_form.html', context)


def new_question(request):
    c = Category.objects.filter(category_name=request.POST.getlist('category')[0]).get()

    q = Question(category=c,question_title=request.POST['questionTitle'], question_text=request.POST['questionText'])

    q.save()

    return HttpResponseRedirect(reverse('questions:index'))


def question_answers(request, question_id):
    logger.debug('question id = ' + question_id)

    question = Question.objects.get(pk=question_id)
    context = {
        'question': question
    }

    return render(request, 'questions/question_answers.html', context)
