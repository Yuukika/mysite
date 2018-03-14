from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from slugify import slugify
from django.core.urlresolvers import reverse
class ArticleColumn(models.Model):
    user = models.ForeignKey(User,related_name='article_column')
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column




class Articletag(models.Model):
    author = models.ForeignKey(User, related_name="tag")
    tag = models.CharField(max_length=50)
    def __str__(self):
        return self.tag




class ArticlePost(models.Model):
    article_tag = models.ManyToManyField(Articletag, related_name="article_tag")
    author = models.ForeignKey(User,related_name="article")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn,related_name="article_column")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)
    users_like = models.ManyToManyField(User, related_name="article_like",blank=True)

    class Mate:
        ordering = ('title',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(ArticlePost,self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id, self.slug])
    def get_url_path(self):
        return reverse('article:list_article_detail', args=[self.id, self.slug])

class Comment(models.Model):
    article = models.ForeignKey(ArticlePost, related_name="comment")
    commentator = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'comment by {} on {}'.format(self.commentator, self.article)
