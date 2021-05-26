# from django.contrib.auth.models import User
from django.db import models


class NumBed(models.Model):
    number_of_bed = models.IntegerField()

    def __str__(self):
        return str(self.number_of_bed) + ' кровати'


class Room(models.Model):
    type_room = models.CharField(max_length=90,
                                 db_index=True,
                                 verbose_name='Тип комнаты')
    num_bed = models.ForeignKey(NumBed,
                                on_delete=models.CASCADE,
                                verbose_name='Количество кроватей')
    description_room = models.TextField(verbose_name='Описание')
    reservation = models.BooleanField(verbose_name='Номер занят')
    free_date = models.DateField(verbose_name='Свободная дата')

    def __str__(self):
        return self.type_room
