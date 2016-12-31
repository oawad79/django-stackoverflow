import logging

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView

from questions.models import Question, Category, QuestionAnswer



logger = logging.getLogger('django')


# def index(request):
#     questions = Question.objects.all()
#     #paginator = Paginator(questions, 10)
#
#     template = loader.get_template('questions/index.html')
#     context = {
#         'questions': questions
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    # test
    question_list = Question.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(question_list, 10)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)


    return render(request, 'questions/index.html', { 'questions': questions })


def question_form(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'questions/question_form.html', context)


def new_question(request):
    c = Category.objects.filter(pk=request.POST.getlist('category')[0]).get()

    q = Question(category=c,
                 question_title=request.POST['questionTitle'],
                 question_text=request.POST['questionText'])

    q.save()

    return HttpResponseRedirect(reverse('questions:index'))


def question_answers(request, question_id):
    logger.debug('question id = ' + question_id)

    question = Question.objects.get(pk=question_id)
    answers = QuestionAnswer.objects.filter(question=question)

    context = {
        'question': question,
        'answers': answers
    }

    return render(request, 'questions/question_answers.html', context)


def add_question_answer(request, question_id):
    logger.debug('an answer received for question = ' + question_id)

    question = Question.objects.get(pk=question_id)
    answer = QuestionAnswer(question=question, answer_text=request.POST['questionAnswer'])
    answer.save()

    url = reverse('questions:question_answers', kwargs={'question_id': question_id})
    return HttpResponseRedirect(url)


def vote_question(request):
    question = Question.objects.get(pk=question_id)
    answers = QuestionAnswer.objects.filter(question=question)

    context = {
        'question': question,
        'answers': answers
    }

    return render(request, 'questions/question_answers.html', context)

