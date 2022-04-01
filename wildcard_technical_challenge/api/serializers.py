from rest_framework import serializers

class CensoredWordsSerializer(serializers.Serializer):
    filtered_words = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    document_text = serializers.CharField(required=True, allow_null=False, allow_blank=False)
