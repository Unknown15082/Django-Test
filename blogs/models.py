from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 256, verbose_name = 'Name')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 256, verbose_name = 'Title')
    body = models.CharField(max_length = 1024, verbose_name = 'Body')
    created_time = models.DateTimeField(verbose_name = "Time created")
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    vote = models.IntegerField(verbose_name = "Number of votes", default = 0)

    def __str__(self):
        return f"{self.title}: {self.body}"