from django.db import models

# Create your models here.
class Manuf(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        db_table = 'manufacture'


class Laptop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gpu = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    storageSize = models.CharField(max_length=255)
    ram = models.IntegerField()
    screenSize = models.FloatField()
    manuf = models.ForeignKey(Manuf, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'laptop'
