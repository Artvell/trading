from django.db import models
from django.contrib.auth import get_user_model

class Individual(models.Model):
    user_id = models.OneToOneField(get_user_model(),verbose_name="Аккаунт", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, verbose_name="Имя", default="")
    last_name = models.CharField(max_length=35, verbose_name="Фамилия", default="")
    #email = models.EmailField(verbose_name="E-mail",max_length=100)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    inn = models.PositiveIntegerField(verbose_name="ИНН")
    passport = models.CharField(max_length=25, verbose_name="Паспорт")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    telegram = models.CharField(max_length=25, verbose_name="Телеграм", blank=True, null=True)
    whats_up = models.CharField(max_length=25, verbose_name="Ватсап", blank=True, null=True)
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"