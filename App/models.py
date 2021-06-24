from django.db import models
from django.db.models.fields import CharField

class Movies(models.Model):

    title = models.CharField(verbose_name="Movie Title", max_length=255, null=True)
    year_of_release = models.IntegerField(verbose_name="Year of Release", null=True)
    
    def __str__(self):
        return self.title

class Inventory(models.Model):

      product = models.IntegerField()
      batchnum = models.IntegerField()
      unitprice = models.FloatField()
      sellingprice = models.FloatField()
      quantity = models.FloatField()
      barcode = models.IntegerField()
      inventory_code = models.IntegerField()
      date = models.DateField()

class Product(models.Model):

      product = models.CharField(max_length=255, null=True)
      uom = models.CharField(max_length=255, null=True)
      barcode = models.IntegerField()

class Purchase(models.Model):

      code = models.CharField(max_length=255, null=True)
      date = models.DateField()
      supplier = models.CharField(max_length=255, null=True)
      total_cost = models.FloatField()

class PurchaseLine(models.Model):

      purchase_parent = models.CharField(max_length=255, null=True)
      product_code = models.CharField(max_length=255, null=True)
      cost_per_unit = models.FloatField()
      quantity = models.FloatField()

class Sales(models.Model):

      customer = models.CharField(max_length=255, null=True)
      ornumber = models.IntegerField()
      totalSale = models.FloatField()
      date = models.DateField()


class SalesLine(models.Model):
      sale_parent = models.CharField(max_length=255, null=True)
      inven_id = models.CharField(max_length=255, null=True)
      product_code = models.CharField(max_length=255, null=True)
      price_per_unit = models.FloatField()
      quantity = models.FloatField()

class Supplier(models.Model):
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    business_type = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=255, null=True)
      