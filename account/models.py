from django.db import models
from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(settings.AUYH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True, verbose_name='о себк')

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return f'профиль пользователя {self.user.last_name} {self.user.first_name}'
