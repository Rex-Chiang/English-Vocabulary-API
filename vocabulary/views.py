import logging
from random import randint
from django.conf import settings
from django.db.models import Count
from rest_framework import status, viewsets
from rest_framework.response import Response
from vocabulary.models import Vocabulary
from vocabulary.serializers import VocabularySerializer

logger = logging.getLogger(settings.LOG_VERSION)

class VocabularyView(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "delete"]
    serializer_class = VocabularySerializer
    lookup_url_kwarg = "en_word"

    def get_queryset(self):
        try:
            row_count = Vocabulary.objects.aggregate(count=Count("id"))["count"]

            if not row_count:
                return {}
            else:
                random_index = randint(0, row_count - 1)
                vocabulary = Vocabulary.objects.all()[random_index]
                return [vocabulary]

        except Exception as exception_message:
            logger.exception(exception_message)
            return Response({"message": exception_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            en_word = request.data.get("en_word")
            vocabulary = Vocabulary.objects.filter(en_word=en_word).first()

            if vocabulary:
                logger.info(f"{en_word} is exist.")
                serializer = VocabularySerializer(vocabulary, data=request.data)
            else:
                serializer = VocabularySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as exception_message:
            logger.exception(exception_message)
            return Response({"message": exception_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, en_word=None):
        vocabulary = Vocabulary.objects.filter(en_word=en_word)
        self.perform_destroy(vocabulary)
        return Response(status=status.HTTP_204_NO_CONTENT)

