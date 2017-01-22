from django.conf.urls import url
from django.contrib import auth
from django.template.backends import django

from . import views

app_name = 'questions'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question_form/$', views.question_form, name='question_form'),
    url(r'^new_question/$', views.new_question, name='new_question'),
    url(r'^question_answers/(?P<question_id>[0-9]+)/$', views.question_answers, name='question_answers'),
    url(r'^add_question_answer/(?P<question_id>[0-9]+)/$', views.add_question_answer, name='add_question_answer'),
    url(r'^vote_question/(?P<question_id>[0-9]+)/$', views.vote_question, name='vote_question'),
    url(r'^vote_answer/(?P<question_id>[0-9]+)/$', views.vote_answer, name='vote_answer'),
    url(r'^change/password/$',views.change_password, name='changepassword'),
    url(r'^users/add$', views.add_user, name='add_user')
]