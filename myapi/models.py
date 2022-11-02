from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=60)
    permission = models.BooleanField()

    def __str__(self):
        return self.name
