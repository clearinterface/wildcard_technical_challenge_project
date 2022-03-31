from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import APIException
import logging
from django.conf import settings
# Create your views here.
from rest_framework.response import Response
from api import utils
from .models import CensoredWords
from api.serializers import CensoredWordsSerializer

logger = logging.getLogger(settings.APPLICATION_NAME)


class CensoredWordsViewSet(viewsets.ModelViewSet):

    serializer_class = [CensoredWordsSerializer]

    def create(self, request, *args, **kwargs):
        try:
            serializer = CensoredWordsSerializer(data=request.data)
            if serializer.is_valid():
                document_text = {}
                cleaned = utils.extraction_of_words(request.data['filtered_words'])
                document_text['censored_text'] = utils.replace_words(cleaned, request.data["document_text"])
                cw = CensoredWords.objects.create(document_text=document_text['censored_text'], filtered_words=request.data['filtered_words'])
                document_text['id'] = cw.id
                return Response(document_text, status=status.HTTP_201_CREATED)
            else:
                raise APIException(serializer.errors)
        except Exception as e:
            # should log exception in sentry or graylog.
            logger.error(e)
            raise APIException(e)

