import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import password_reset_confirm, password_reset
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView

from questions.forms import ChangePasswordForm, UserRegistrationForm
from questions.models import Question, Category, QuestionAnswer, UserProfile

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


@login_required(login_url="questions/login/")
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


def vote_question(request, question_id):


    is_up = request.POST['up'] == 'true'
    is_down = request.POST['down'] == 'true'
    is_starred = request.POST['star'] == 'true'

    logger.debug('******* up = ' + str(is_up))
    logger.debug('******* down = ' + str(is_down))
    logger.debug('******* star = ' + str(is_starred))

    question = Question.objects.get(pk=question_id)

    if is_up:
        logger.debug('+1')
        question.votes += 1
    elif is_down:
        logger.debug('-1')
        question.votes -= 1
    elif is_starred:
        question.favorites += 1
    elif not is_starred:
        question.favorites -= 1

    question.save()

    answers = QuestionAnswer.objects.filter(question=question)

    context = {
        'question': question,
        'answers': answers
    }

    return render(request, 'questions/question_answers.html', context)

def vote_answer(request, question_id):
    is_up = request.POST['up'] == 'true'
    is_down = request.POST['down'] == 'true'
    is_starred = request.POST['star'] == 'true'

    question = Question.objects.get(pk=question_id)
    answer = question.questionanswer_set.filter(pk=request.POST['id']).get()

    if is_up:
        logger.debug('+1')
        answer.votes += 1
    elif is_down:
        logger.debug('-1')
        answer.votes -= 1
    elif is_starred:
        answer.favorites += 1
    elif not is_starred:
        answer.favorites -= 1

    answer.save()

    answers = QuestionAnswer.objects.filter(question=question)

    context = {
        'question': question,
        'answers': answers
    }

    return render(request, 'questions/question_answers.html', context)

@login_required
def change_password(request):
    newpassword = request.POST.get("newpassword")
    renewpasssword = request.POST.get("renewpasssword")
    username=request.user.username
    if newpassword == renewpasssword:
        if request.method == 'GET':
            form = ChangePasswordForm()
        else:
            u = User.objects.get(username__exact=username)
            u.set_password(newpassword)
            u.save()
            return redirect('/users/account')
    else:
        return redirect('/change/password/')
    return render(request,'changepassword.html', {'form': form,})

def add_user(request):
    username = request.POST.get("username")
    email = request.POST.get("emailid")
    password = request.POST.get("password")
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    address = request.POST.get("address")
    phone = request.POST.get("phone")
    #print ".........address........",address
    if request.method == 'GET':
        form = UserRegistrationForm() #object creation
    else:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
              user = User.objects.create_user(username, email, password)
              user.first_name = fname
              user.last_name = lname
              user.save()
              a = UserProfile(user_id=user.id,address=address,phone=phone)
              a.save()
              return redirect('questions:index')
    return render(request, 'registration.html', {'form': form,})

@login_required
def change_password(request):
    newpassword = request.POST.get("newpassword")
    renewpasssword = request.POST.get("renewpasssword")
    username=request.user.username
    if newpassword == renewpasssword:
        if request.method == 'GET':
            form = ChangePasswordForm()
        else:
            u = User.objects.get(username__exact=username)
            u.set_password(newpassword)
            u.save()
            return redirect('/login')
    else:
        return redirect('changepassword')
    return render(request, 'registration/password_change_form.html', {'form': form, })
