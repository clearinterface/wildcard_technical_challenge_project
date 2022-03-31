from django.db import models


# Create your models here.
class CensoredWords(models.Model):

    filtered_words = models.CharField(max_length=1000, blank=False, null=False)
    document_text = models.TextField(blank=False)
