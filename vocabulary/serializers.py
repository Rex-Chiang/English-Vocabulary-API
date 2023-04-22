from vocabulary.models import Vocabulary
from rest_framework import serializers

class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ["en_word", "cn_word", "example"]