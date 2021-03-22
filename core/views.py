from django.shortcuts import render
from articles import models

# Create your views here.
def home(request):

    articles = models.Article.objects.filter(status="작성완료").order_by('-display_date')[:9]
    return render(request, "home.html", context={"articles": articles} ) 


def policy(request):

    return render(request, "policy.html")


def purpose(request):

    return render(request, "purpose.html")


def announce(request):

    return render(request, "announce.html")


def news(request):

    return render(request, "news.html")


def donation_status(request):

    return render(request, "donation_status.html")
