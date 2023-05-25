from django.db import models


class UserTask(models.Model):
    title = models.CharField(("Title"), max_length=50)
    key = models.IntegerField(("Key"))
    details = models.CharField(("Comments"), max_length=150)
    active = models.BooleanField(("Active"), default=True)
