from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save


User = get_user_model()


class Post(models.Model):

    title = models.CharField(max_length=128, verbose_name='main')
    body = models.TextField(verbose_name='novel')
    draft = models.BooleanField(default=True)
    changed_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='autor')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def __str__(self):
        return self.title
 
 
    
def post_save_dispatcher(sender, **kwargs):
    inst = kwargs['instance']  # instance, created, raw, update_fields
    if kwargs['created']:
        print(f'+++ былы создана запись {inst.title}\n+++ содержащая следующий текст: {inst.body[:40]}...')
    else:
        print(f'+++ запись {inst.title}\n+++ содержащая следующий текст: {inst.body[:40]}...\n+++ была обновлена')
    
    
post_save.connect(post_save_dispatcher, sender=Post)