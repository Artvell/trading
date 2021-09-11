from django.db import models

class NewsCategory(models.Model):
    objects = models.Manager()
    name = models.CharField(verbose_name="Название", max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"