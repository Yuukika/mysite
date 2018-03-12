from django.shortcuts import render
from .models import BlogArticles

def blog_title(request):
    blogs =BlogArticles.objects.all()
    return render(request,'blog/title.html',{'blogs': blogs})

def blog_content(request, article_id):
    article = BlogArticles.objects.get(id = article_id)
    return render(request, 'blog/article.html', {'article': article})