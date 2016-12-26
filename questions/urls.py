from django.conf.urls import url
from . import views

app_name = 'questions'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question_form/$', views.question_form, name='question_form'),
    url(r'^new_question/$', views.new_question, name='new_question'),
    url(r'^question_answers/(?P<question_id>[0-9]+)/$', views.question_answers, name='question_answers'),
    url(r'^add_question_answer/(?P<question_id>[0-9]+)/$', views.add_question_answer, name='add_question_answer')

]