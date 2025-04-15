from django.db import models
from django.utils import timezone


class News(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Содержимое")
    created_at = models.DateTimeField("Дата публикации", default=timezone.now)
    is_published = models.BooleanField("Опубликовано", default=True)
    image = models.ImageField("Изображение", upload_to="news/", blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
