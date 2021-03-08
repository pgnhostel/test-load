from django.db import models


class Pgs(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics', null=True, blank=True)

    def __str__(self):
        return self.name
