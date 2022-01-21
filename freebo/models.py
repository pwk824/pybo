from django.db import models
from django.contrib.auth.models import User


class Freewriting(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title



class Replying(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    freewriting = models.ForeignKey(Freewriting, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
