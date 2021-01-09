from django.db import models
import datetime 
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    article_title = models.CharField('Article\'s Title', max_length=200)
    article_text = models.TextField('Article\'s Description')
    pub_date = models.DateTimeField('Publication Data')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days =  7))

    class Meta: 
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Author\'s Name', max_length=50)
    comment_text = models.CharField('Author\'s Comment', max_length=200)


    def __str__(self):
        return self.author_name
    

    class Meta: 
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'