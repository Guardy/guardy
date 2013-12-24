from django.db import models
import refresher


class Program(models.Model):

    name = models.CharField(max_length=30)
    version = models.CharField(max_length=127)
    url = models.CharField(max_length=255)
    refresh_function_name = models.CharField(max_length=30)

    def refresh(self):
        func = getattr(refresher, self.refresh_function_name)
        func(self)
        self.save()

    def __unicode__(self):
        return self.name