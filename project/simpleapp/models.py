from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


# Новость для прочтения
class New(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True, # названия новстей не должны повторяться
    )
    description = models.TextField()

    date_pub = models.DateField(auto_now_add=True)


    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news', # все новости в категории будут доступны через поле news
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('new_detail', args=[str(self.id)])


# Категория, к которой будет привязываться новость
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


