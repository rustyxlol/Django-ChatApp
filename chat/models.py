from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=50)
    # for url
    slug = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)
