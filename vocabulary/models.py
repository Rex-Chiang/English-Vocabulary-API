import uuid
from django.db import models
from django.utils import timezone

class Vocabulary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    en_word = models.CharField(max_length=32, unique=True)
    cn_word = models.CharField(max_length=32)
    example = models.CharField(max_length=256, default="No Example", blank=True)
    add_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "vocabulary"
        indexes = [
            models.Index(fields=["en_word"], name="en_word_idx")
        ]
