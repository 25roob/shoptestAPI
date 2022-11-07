from django.db import models

# Create your models here.

class Category(models.Model):
    # id = models.UUIDField()
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return '{} {}'.format(self.id, self.name)


class Product(models.Model):
    # id = models.UUIDField()
    name = models.CharField(max_length=250)
    url_image = models.CharField(max_length=250)
    price = models.FloatField()
    discount = models.IntegerField()
    category = models.ForeignKey("Category", verbose_name='products', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{} {}'.format(self.id, self.name)