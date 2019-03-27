from django.db import models

from django.db import models


class Article(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'media/', default = 'media/no-img.jpg')
    prix = models.FloatField(default=0.0)
    description = models.TextField()

