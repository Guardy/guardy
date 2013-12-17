from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    avatar = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class PostManager(models.Manager):

    def get_query_set(self):
        return super(PostManager, self).get_query_set().order_by('date_time')


class Post(models.Model):
    header = models.CharField(max_length=127)
    date_time = models.DateTimeField()
    preview = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(Author)
    # objects = PostManager()

    def __unicode__(self):
        return self.header
