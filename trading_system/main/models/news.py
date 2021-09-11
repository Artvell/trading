from django.db import models
from main.models import NewsCategory
from datetime import date

class News(models.Model):
    objects = models.Manager()
    title = models.CharField(verbose_name="Заголовок",max_length=50)
    text = models.TextField(verbose_name="Текст")
    photo = models.ImageField(verbose_name="Фотография", null=True, blank=True)
    categories = models.ManyToManyField(NewsCategory,verbose_name="Категории", related_name="news")
    date = models.DateField(verbose_name="Дата", default=date.today())
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"