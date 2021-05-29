from django.db import models

# Create your models here.
from django.db.models import Q


class FlashCard(models.Model):
    owner = models.TextField()

    title = models.TextField()

    subject = models.TextField()

    content = models.TextField()

    date = models.DateTimeField(auto_now_add=True)

    private = models.BooleanField( db_index=True, default=False)

    class Meta:
        indexes = [models.Index(fields=['private'],name="public_flashcards_index",condition=Q(private = False)) ]



