from django.db import models
from main.models import Product, product
from django.contrib.auth import get_user_model

class Deal(models.Model):
    objects = models.Manager()
    choices = (
        ("Заявка","Заявка"),
        ("Ожидает оплаты","Ожидает оплаты"),
        ("Оплачена","Оплачена"),
        ("Исполнена","Исполнена"),
        ("Аннулирована","Аннулирована"),
        ("Блокирована","Блокирована"),
    )
    type_choices = (
        ("Продажа","Продажа"),
        ("Покупка", "Покупка")
    )
    user_id = models.OneToOneField(get_user_model(),verbose_name="Аккаунт", on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT,verbose_name="Товар")
    status = models.CharField(max_length=15, choices=choices, verbose_name="Статус")
    type = models.CharField(max_length=7,choices=type_choices, verbose_name="Тип")
    cost = models.FloatField(verbose_name="Цена")
    volume = models.FloatField(verbose_name="Объём")
    summ = models.FloatField(verbose_name="Сумма")
    delivery_time = models.CharField(max_length=50, verbose_name="Срок поставки")
    shipment = models.CharField(max_length=50, verbose_name="Отгрузка")

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"
