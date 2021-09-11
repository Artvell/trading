from django.db import models
from django.contrib.auth import get_user_model

class Entity(models.Model):
    user_id = models.OneToOneField(get_user_model(),verbose_name="Аккаунт", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Название компании")
    mfo = models.PositiveIntegerField(verbose_name="МФО")
    inn = models.PositiveIntegerField(verbose_name="ИНН")
    checking_account = models.CharField(max_length=50, verbose_name="Расчетный счет")
    bank = models.CharField(max_length=100, verbose_name="Банк")
    address = models.CharField(max_length=255, verbose_name="Адрес")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = "Юридические лица"
