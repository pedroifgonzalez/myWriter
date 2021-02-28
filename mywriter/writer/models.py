from django.db import models

class Writing(models.Model):

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    creation_date = models.DateField(auto_now=True)
    modification_date = models.DateField()

    def __str__(self):
        return self.title

class Author(models.Model):

    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
