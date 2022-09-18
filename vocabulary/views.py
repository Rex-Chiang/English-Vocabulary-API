import random
import logging
from django.conf import settings
from django.db.models import Max
from rest_framework import status, viewsets
from rest_framework.response import Response
from vocabulary.models import Vocabulary
from vocabulary.serializers import VocabularySerializer

logger = logging.getLogger(settings.LOG_VERSION)

class VocabularyView(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "delete"]
    serializer_class = VocabularySerializer
    lookup_url_kwarg = "english_word"

    def get_queryset(self):
        max_id = Vocabulary.objects.aggregate(max_id=Max("id"))["max_id"]

        if not max_id:
            return {}

        while True:
            pk = random.randint(1, max_id)
            vocabulary = Vocabulary.objects.filter(pk=pk)

            if vocabulary:
                return vocabulary

    def create(self, request, *args, **kwargs):
        try:
            english_word = request.data.get("english_word")
            vocabulary = Vocabulary.objects.filter(english_word=english_word)

            if vocabulary.exists():
                logger.info(f"{english_word} is exist.")
                serializer = VocabularySerializer(vocabulary.first(), data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
                else:
                    logger.error(serializer.errors)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def destroy(self, request, english_word=None):
        instance = Vocabulary.objects.filter(english_word=english_word)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

