from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=30)
    version = models.CharField(max_length=127)
    url = models.CharField(max_length=255)

    def refresh(self, function):
        function(self)

    def __unicode__(self):
        return self.name