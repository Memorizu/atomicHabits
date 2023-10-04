from django.db import models

from constants import NULLABLE


class Habit(models.Model):
    class Frequency(models.TextChoices):
        EACH_HOUR = 'each hour', 'каждый час'
        DAILY = 'daily', 'Раз в день'
        WEEKLY = 'weekly', 'Раз в неделю'

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='owner', related_name='habits')
    place = models.CharField(max_length=255, verbose_name='place')
    lead_time = models.DateTimeField(verbose_name='lead_time')
    action = models.TextField(verbose_name='action')
    is_pleasant = models.BooleanField(verbose_name='is_pleasant', default=True)
    related_habit =  models.ForeignKey('self', **NULLABLE, on_delete=models.SET_NULL, verbose_name='related_habit')
    frequency = models.CharField(
        max_length=50,
        choices=Frequency.choices,
        default=Frequency.DAILY,
        verbose_name='frequency'
    )
    reward = models.TextField(**NULLABLE, verbose_name='reward')
    time_to_complete = models.DateTimeField(verbose_name='time_to_complete')
    is_public = models.BooleanField(default=False, verbose_name='is_public')

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'
