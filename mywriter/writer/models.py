from django.contrib.auth.models import User
from django.db import models

class Writing(models.Model):

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    creation_date = models.DateField(auto_now=True)
    modification_date = models.DateField(null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Author(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


__all__ = ['Writing', 'Author']