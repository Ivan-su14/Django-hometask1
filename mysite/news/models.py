from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField('Заголовок',max_length=50)
    content = models.TextField('Описание',blank=True)
    created = models.DateTimeField('Дата создания',auto_now_add=True)
    updated = models.DateTimeField('Датат изменения', auto_now=True, blank=True)
    photo = models.ImageField('Фото', upload_to='photo/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']