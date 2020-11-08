from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Poll(models.Model):
    question = RichTextField(blank=True, null=True)
    qs_one = models.CharField(max_length=30)
    qs_two = models.CharField(max_length=30)
    qs_three = models.CharField(max_length=30)
    qs_one_cnt = models.IntegerField(default=0)
    qs_two_cnt = models.IntegerField(default=0)
    qs_three_cnt = models.IntegerField(default=0)

    def total(self):
        return self.qs_one_cnt + self.qs_two_cnt + self.qs_three_cnt
