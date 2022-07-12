from django.db import models
from django.utils import timezone
import datetime


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Collection(TimeStampModel):
    name = models.CharField(max_length=250)
    slug = models.SlugField()


class Task(TimeStampModel):
    description = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, related_name='collection_task', on_delete=models.CASCADE)

    def __str__(self):
        return self.description
