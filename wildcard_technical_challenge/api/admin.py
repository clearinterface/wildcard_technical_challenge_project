from django.contrib import admin

# Register your models here.
from .models import CensoredWords


class CensoredWordsAdmin(admin.ModelAdmin):
    fields = ['filtered_words', 'document_text']
    list_display = ('filtered_words',)


admin.site.register(CensoredWords, CensoredWordsAdmin)