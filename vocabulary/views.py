import logging
from django.conf import settings
from rest_framework import status, viewsets
from rest_framework.response import Response
from vocabulary.models import Vocabulary
from vocabulary.serializers import VocabularySerializer

logger = logging.getLogger(settings.LOG_VERSION)

class VocabularyView(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    serializer_class = VocabularySerializer

    def get_queryset(self):
        vocabulary = Vocabulary.objects.filter(english_word=self.request.GET.get("english_word"))

        if vocabulary:
            return vocabulary
        else:
            return None

    def create(self, request, *args, **kwargs):
        try:
            if Vocabulary.objects.filter(english_word=request.data.get("english_word")).exists():
                return Response({"message": "Already Exists"}, status=status.HTTP_409_CONFLICT)

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

