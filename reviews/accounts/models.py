from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to=get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='Профиль пользователя'
    )

    def __str__(self):
        return f'Профиль пользователя {self.user.get_full_name()}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
