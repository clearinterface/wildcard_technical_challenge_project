from django.db import models


# Create your models here.
class CensoredWords(models.Model):
    word_identifier = models.CharField(max_length=100, blank=False, null=False)
    word_list = models.TextField(blank=False)
    date_added = models.DateField()
    active = models.BooleanField(default=True)