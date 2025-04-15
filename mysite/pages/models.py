from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    # content = models.TextField()
    content = RichTextField()
    image = models.ImageField(upload_to="pages/", blank=True, null=True)
    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.CharField(max_length=255, blank=True)
    show_in_menu = models.BooleanField(default=True)

    def __str__(self):
        return self.title
