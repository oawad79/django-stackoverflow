from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=5)
    category_desc = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name + ' : ' + self.category_desc


class Question(models.Model):
    question_title = models.CharField(max_length=200, default='')
    question_text = models.CharField(max_length=1000)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, default=1)

    def __str__(self):
        return self.question_title

class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text





