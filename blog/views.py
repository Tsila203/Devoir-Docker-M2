from django.shortcuts import render
from .models import Article

def home(request):
    list_articles = Article.objects.all().order_by('-created_at')
    context = {"liste_articles": list_articles}
    return render(request, "index.html", context)

def detail(request, id_article):
    article = Article.objects.get(id = id_article)
    return render(request, "detail.html", {"article": article})  