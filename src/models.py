from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    comments = models.TextField()
    publish_date  = models.DateTimeField()
    author_name = models.CharField(max_length = 70)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post);
    publish_date = models.DateTimeField(default=timezone.now())
    description = models.TextField()

    def __str__(self):
        return self.post
