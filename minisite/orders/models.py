from django.db import models


class SalesOrder(models.Model):
    amount = models.IntegerField()
    decription = models.CharField(max_length=255)