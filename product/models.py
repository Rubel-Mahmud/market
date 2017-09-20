from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.name


class Choice(models.Model):
    product = models.ForeignKey(Product)
    brand = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

