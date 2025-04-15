from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News
from news.models import News


# def some_view(request):
#     news = News.objects.filter(is_published=True)[:3]
#     return render(request, "your_template.html", {"news": news})


def news_list(request):
    news = News.objects.filter(is_published=True)
    paginator = Paginator(news, 6)  # по 6 новостей на странице
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "news/news_list.html", {"page_obj": page_obj})
