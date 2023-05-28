from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='main', blank=True)
    body = models.TextField(verbose_name='novel')
    draft = models.BooleanField(default=False)
    changed_at = models.DateTimeField()
    changed_at = models.DateTimeField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='autor')
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def __str__(self):
        return self.title