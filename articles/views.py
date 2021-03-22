from django.shortcuts import render
from . import models

# Create your views here.
def announce(request):

    articles_announce = models.Article.objects.filter(board="공지사항")
    return render(request, "announce.html", context={"articles": articles_announce})


def news(request):

    articles_news = models.Article.objects.filter(board="동문소식")
    return render(request, "news.html", context={"articles": articles_news})


def detail(request, pk):

    article = models.Article.objects.get(pk=pk)
    return render(request, "article.html", context={"article": article})