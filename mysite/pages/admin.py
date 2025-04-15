from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "show_in_menu")
    fields = (
        "title",
        "slug",
        "content",
        "image",
        "seo_title",
        "seo_description",
        "show_in_menu",
    )
    search_fields = ("title", "slug")
    list_filter = ("show_in_menu",)
    list_editable = ("show_in_menu",)
    ordering = ("title",)
    list_per_page = 10
    save_on_top = True
