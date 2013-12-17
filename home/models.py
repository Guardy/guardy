from django.db import models


class Article(models.Model):
    header = models.CharField(max_length=127)
    content = models.TextField()

    def __unicode__(self):
        return self.header

