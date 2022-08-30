from django.db import models
from django.utils import timezone

class Vocabulary(models.Model):
    id = models.AutoField(primary_key=True)
    english_word = models.CharField(max_length=32, unique=True)
    chinese_word = models.CharField(max_length=32)
    add_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "vocabulary"
        indexes = [
            models.Index(fields=['english_word'], name='english_word_idx')
        ]
