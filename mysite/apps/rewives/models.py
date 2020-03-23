import datetime
from django.db import models

from django.utils import timezone


class Comment(models.Model):  # база данных для комментариев

    author_name = models.CharField('Автор комментария', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=300)
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.author_name

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:  # переименовать с англ
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
