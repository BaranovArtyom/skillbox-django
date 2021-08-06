from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
