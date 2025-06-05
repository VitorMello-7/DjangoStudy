import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

# Note: The models above define a simple poll application with two models:
# Question and Choice. The Question model has a text field for the question and a date field for when it was published.
# The Choice model is linked to the Question model via a foreign key and includes a text field for the choice and an integer field for the number of votes.
# These models can be used to create a basic polling system where users can vote on different choices for each question.
# The __str__ methods provide a string representation of the objects, which is useful for displaying them in the Django admin interface or in templates.

    