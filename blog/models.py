from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.FileField(upload_to='uploads/%Y/%m/%d', default='uploads/default-post.png')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def upvote(self):
        self.score = self.score + 1

    def downvote(self):
        self.score = self.score - 1

    def __str__(self):
        return self.title

