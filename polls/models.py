# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone
from pip._vendor.six import python_2_unicode_compatible


@python_2_unicode_compatible  # 兼容python2。 __str__(self)  ---> __unicode__(self)
class Question(models.Model):
    question_text = models.CharField('请输入问题', max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name="属于哪个问题")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
