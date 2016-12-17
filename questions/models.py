from django.db import models

# Create your models here.

class Question(models.Model):
    question_title = models.CharField(max_length=200, default='')
    question_text = models.CharField(max_length=1000)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.question_title

class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text


