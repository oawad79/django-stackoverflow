from django.conf.urls import url
from . import views

app_name = 'questions'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question_form/$', views.question_form, name='question_form'),
    url(r'^new_question/$', views.new_question, name='new_question')
]