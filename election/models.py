from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
