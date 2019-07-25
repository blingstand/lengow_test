from django.db import models

# Create your models here.
class Marketplace(models.Model):

    name = models.CharField(max_length=100)


class Order(models.Model):
    order_id = models.ForeignKey('Status', on_delete=models.CASCADE)
    marketplace_id = models.ForeignKey('Marketplace', on_delete=models.CASCADE)
    date_hour = models.DateTimeField(verbose_name="Date de la commande")
    amount = models.CharField(max_length=100)

    class Meta:
        ordering = ['date_hour']#je veux la date en premier

class Status(models.Model):

    marketplace = models.CharField(max_length=100)
    lengow = models.CharField(max_length=100)
