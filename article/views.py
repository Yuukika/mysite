from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import ArticleColumn,ArticlePost, Articletag
from .forms import ArticleColumnForm, ArticlePostForm, ArticleTagForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

@csrf_exempt
@login_required(login_url='/account/login/')
def article_column(request):
    if request.method == 'GET':
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        return render(request,"article/column/article_column.html",{"columns":columns,'column_form': column_form})
    if request.method == "POST":
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id = request.user.id,column = column_name)
        if columns:
            return HttpResponse("2")
        else:
            ArticleColumn.objects.create(user = request.user, column=column_name)
            return HttpResponse("1")

@login_required(login_url="/account/login/")
@require_POST
@csrf_exempt
def rename_article_column(request):
    column_id = request.POST["column_id"]
    column_name = request.POST["column_name"]
    try:
        column = ArticleColumn.objects.get(id=column_id)
        column.column = column_name
        column.save()
        return HttpResponse('1')
    except:
        return HttpResponse("0")


@login_required(login_url="/account/login/")
@require_POST
@csrf_exempt
def delete_article_column(request):
    column_id = request.POST["column_id"]
    try:
        column = ArticleColumn.objects.get(id=column_id)
        column.delete()
        return HttpResponse('1')
    except:
        return HttpResponse("0")


@login_required(login_url="/account/login/")
@csrf_exempt
def article_post(request):
    if request.method == "POST":
        article_post_form =ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                article = article_post_form.save(commit=False)
                article.author = request.user
                article.column = request.user.article_column.get(id = request.POST['column_id'])
                tags = request.POST["tags"]
                article.save()
                if tags:
                    for atag in json.loads(tags):
                        tag = request.user.tag.get(tag=atag)
                        article.article_tag.add(tag)
                return HttpResponse("1")
            except:
                return HttpResponse("2")
        else:
            return HttpResponse("3")

    else:
        article_post_form = ArticlePostForm()
        article_columns = request.user.article_column.all()
        article_tags = request.user.tag.all()
        return render(request, 'article/column/article_post.html',{"article_post_form":article_post_form,"article_columns":article_columns, 'article_tags':article_tags})


@login_required(login_url="/account/login")
def article_list(request):
    article_list = ArticlePost.objects.filter(author=request.user)
    paginator = Paginator(article_list,2)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        article_list = current_page.object_list
    except PageNotAnInteger:
        current_page =paginator.page(1)
        article_list = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        article_list = current_page.object_list
    return render(request, 'article/column/article_list.html',{'article_list':article_list,'page':current_page})

@login_required(login_url="account/login")
def article_detail(request, id, slug):
    article =get_object_or_404(ArticlePost, id=id, slug=slug)
    return render(request,'article/column/article_detail.html',{'article':article})

@login_required(login_url="/account/login")
@csrf_exempt
@require_POST
def delete_article(request):
    article_id = request.POST['article_id']
    try:
        article = ArticlePost.objects.filter(id=article_id)
        article.delete()
        return HttpResponse('1')

    except:
        return HttpResponse('0')



@login_required(login_url="/account/login")
@csrf_exempt
def edit_article(request, article_id):
    if request.method == "GET":
        article = ArticlePost.objects.get(id = article_id)
        columns = ArticleColumn.objects.all()
        article_form = ArticlePostForm(initial={'title':article.title,})
        return render(request, 'article/column/edit_article.html', {'article':article,'columns':columns, 'article_form':article_form})
    else:
        article = ArticlePost.objects.get(id = article_id)
        try:
            article.column = request.user.article_column.get(id = request.POST['column_id'])
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return HttpResponse("1")
        except:
            return HttpResponse("0")

@login_required(login_url="/account/login/")
@csrf_exempt
def article_tag(request):
    if request.method == "GET":
        articletagform = ArticleTagForm()
        tags = Articletag.objects.filter(author=request.user)
        return render(request, 'article/tag/tag_list.html', {'articletagform':articletagform, 'tags':tags})
    if request.method == "POST":
        articletagform = ArticleTagForm(data=request.POST)
        if articletagform.is_valid():
            try:
                new_tag = articletagform.save(commit=False)
                new_tag.author = request.user
                new_tag.save()
                return HttpResponse("1")
            except:
                return HttpResponse('cant save your tag')
        else:
            return HttpResponse("sorry the form is not valid")

@login_required(login_url="/account/login/")
@require_POST
@csrf_exempt
def rename_article_tag(request):
    tag_id = request.POST["tag_id"]
    tag_name = request.POST["tag_name"]
    try:
        tag = Articletag.objects.get(id=tag_id)
        tag.tag = tag_name
        tag.save()
        return HttpResponse('1')
    except:
        return HttpResponse("0")


@login_required(login_url="/account/login/")
@require_POST
@csrf_exempt
def delete_article_tag(request):
    tag_id = request.POST["tag_id"]
    try:
        tag = Articletag.objects.get(id=tag_id)
        tag.delete()
        return HttpResponse('1')
    except:
        return HttpResponse("0")

