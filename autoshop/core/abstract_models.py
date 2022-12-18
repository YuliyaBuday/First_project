from django.db import models


class BaseModel(models.Model):
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True