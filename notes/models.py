from django.db import models
from uuid import uuid4

# Create your models here.

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    #TODO: Add user/author
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #TODO: Tags