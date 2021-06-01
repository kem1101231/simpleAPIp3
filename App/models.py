from django.db import models

class Movies(models.Model):

    title = models.CharField(verbose_name="Movie Title", max_length=255, null=True)
    year_of_release = models.IntegerField(verbose_name="Year of Release", null=True)
    
    def __str__(self):
        return self.title