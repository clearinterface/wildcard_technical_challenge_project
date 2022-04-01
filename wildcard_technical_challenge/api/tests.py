from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.


class CensoredWordsTest(APITestCase):
    def test_valid_censored_words_double_quotes(self):
        url = "http://127.0.0.1:8000/api/words/"
        data = {"filtered_words": "\"there is a dog\", chicken, \"human being\" know", "document_text": "there comes a time, there is a dog and secret dog, chicken"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["censored_text"], "there comes a time, XXXX and secret dog, XXXX")

    def test_missing_filtered_words(self):
        url = "http://127.0.0.1:8000/api/words/"
        data = {"filtered_words": "", "document_text": "'''there comes a time, there is a dog and secret dog, chicken"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['detail'], "{'filtered_words': [ErrorDetail(string='This field may not be blank.', code='blank')]}")

    def test_valid_censored_words_single_quotes(self):
        url = "http://127.0.0.1:8000/api/words/"
        data = {"filtered_words": "'there is a dog', chicken, 'human being' know CIA, many", "document_text": "there comes a time, there is a dog and secret dog, chicken CIA"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["censored_text"], "there comes a time, XXXX and secret dog, XXXX XXXX")

