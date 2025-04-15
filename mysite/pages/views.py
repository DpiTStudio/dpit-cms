from django.shortcuts import render, get_object_or_404
from .models import Page


def home(request):
    pages = Page.objects.filter(show_in_menu=True)
    return render(request, "home.html", {"pages": pages})


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    pages = Page.objects.filter(show_in_menu=True)
    return render(request, "page_detail.html", {"page": page, "pages": pages})
