from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    description = models.TextField(max_length=1000, default='', verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey('Author', default=None, null=True, on_delete=models.CASCADE)
    rubric = models.ForeignKey('Rubric', default=None, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_advertisements'
        ordering = ['id']

class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50, default='Unnamed', verbose_name='Имя')
    email = models.CharField(max_length=30, default='mail@mail.com', verbose_name='Почта')
    telephone = models.CharField(max_length=11, verbose_name='Телефон')

    def __str__(self):
        return self.name

class Rubric(models.Model):
    name = models.CharField(max_length=50, default='No rubric', verbose_name='Рубрика')

    def __str__(self):
        return self.name