from django.db import models
from django.utils.timezone import now
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return now() - datetime.timedelta(days=1) <= self.pub_date

    def verbose_question_text(self):
        return 'Question: %s' % self.question_text

    class Meta:
        ordering = ("-pub_date", )


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices',
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def choices(self):
        if not hasattr(self, '_choices'):
            self._choices = self.choices.all()
        return self._choices

# Create your models here.
