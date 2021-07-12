from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()

    def __str__(self):
        return self.title


class Forums(models.Model):
    Name = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 100)
    Topic = models.CharField(max_length = 100, unique=True)
    Description = models.CharField(max_length = 1000)
    Link = models.CharField(max_length = 100)

    def __str__(self):
        return self.Topic

class Discussion(models.Model):
    Forum = models.ForeignKey(Forums, on_delete = models.CASCADE)
    Name = models.CharField(max_length = 100, default = None)
    Discuss = models.CharField(max_length = 1000)