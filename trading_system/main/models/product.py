from django.db import models
from jsonfield import JSONField
from jsonfield.utils import default

class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(verbose_name="Наименование", max_length=50)
    specifications = models.TextField(verbose_name="Спецификации", default="")
    percent = models.FloatField(verbose_name="Процент", default=0.0)
    brokerage_commission = models.FloatField(verbose_name="Брокерская комиссия", default=0.0)
    exchange_commission = models.FloatField(verbose_name="Биржевая комиссия", default=0.0)
    due_date = models.FloatField(verbose_name="Срок оплаты полной суммы", default=0.0)
    delivery_time = models.FloatField(verbose_name="Срок поставки", default=0.0)
    processing_time = models.FloatField(verbose_name="Срок обработки заявки", default=0.0)
    dates = JSONField(default=[])
    opening = JSONField(default=[])
    max_data = JSONField(default=[])
    min_data = JSONField(default=[])
    closing = JSONField(default=[])
    volume = JSONField(default=[])

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"