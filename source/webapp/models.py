from django.db import models
from django.contrib.auth import get_user_model
STATUS_CHOICES = [('for_moderation', 'На модерацию'), ('published', 'опубликовано'), ('rejected', 'Отклонено'), ('for_delete', 'На удаление')]
# Create your models here.


class Category(models.Model):
    categoryname = models.CharField(max_length=150, null=False, blank=False, verbose_name="Категория")

    def __str__(self):
        return f'{self.categoryname}'
class Ads(models.Model):
    picture = models.ImageField(null=True, blank=True, upload_to='picture', verbose_name='Картинка')
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=2000, verbose_name='Описание', null=True, blank=True)
    ads_author = models.ForeignKey(get_user_model(), related_name='author' , on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey('webapp.Category', related_name='category', on_delete=models.PROTECT, verbose_name="Категория")
    price = models.PositiveIntegerField(null=False, blank=False, verbose_name='Цена')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0],
                                verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

class Comment(models.Model):
    ad = models.ForeignKey('webapp.Ads', related_name='comment', on_delete=models.CASCADE,
                                verbose_name='Комментарий')
    text = models.TextField(max_length=2000, verbose_name='Текст', null=False, blank=False)
    comment_author = models.ForeignKey(get_user_model(), related_name='comment_author', on_delete=models.CASCADE,
                               verbose_name='Автор', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
