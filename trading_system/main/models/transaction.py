from django.db import models
from django.contrib.auth import get_user_model
from main.models import Deal

class Transaction(models.Model):
    choices = (
        ("Приход","Приход"),
        ("Расход","Расход")
    )
    user = models.ForeignKey(get_user_model(),verbose_name="Аккаунт", on_delete=models.PROTECT)
    title = models.CharField(max_length=100, verbose_name="Название транзакции")
    type = models.CharField(max_length=6,verbose_name="Тип",choices=choices)
    summ = models.FloatField(verbose_name="Сумма")
    date = models.DateField(verbose_name="Дата")
    deal = models.OneToOneField(Deal, verbose_name="Сделка", blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
