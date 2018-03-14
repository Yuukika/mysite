from django.conf.urls import url
from . import views, list_views

urlpatterns = [
    url(r'^$', list_views.article_list, name='article_titles'),
    url(r'^article-column/$',views.article_column,name='article_column'),
    url(r'^rename-article-column/$',views.rename_article_column,name='rename_article_column'),
    url(r'^delete-article-column/$',views.delete_article_column,name='delete_article_column'),
    url(r'^article-post/$',views.article_post,name='article_post'),
    url(r'^article-list/$',views.article_list,name='article_list'),
    url(r'^article-list/(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.article_detail,name='article_detail'),
    url(r'^delete-article/$', views.delete_article, name="delete_article"),
    url(r'^edit-article/(?P<article_id>\d+)/$', views.edit_article, name="edit_article"),
    url(r'^list-article-titles/$', list_views.article_list, name="article_titles"),
    url(r'^list-article-titles/(?P<username>[-\w]+)/$', list_views.article_list, name="author_article"),
    url(r'^list-article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',list_views.article_detail,name='list_article_detail'),
    url(r'^like-article/$', list_views.like_article, name="like_article"),
    url(r'^article-tag/$', views.article_tag, name="article_tag"),
    url(r'^rename-article-tag/$',views.rename_article_tag,name='rename_article_tag'),
    url(r'^delete-article-tag/$',views.delete_article_tag,name='delete_article_tag'),
]