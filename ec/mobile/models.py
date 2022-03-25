from django.db import models

# Create your models here.
class Mobile(models.Model):
    id = models.AutoField(primary_key=True)
    cpu = models.CharField(max_length=255)
    gpu = models.CharField(max_length=255)
    storageSize =models.IntegerField()
    screenSize = models.FloatField()
    screenResolution = models.CharField(max_length=255)
    ramSize = models.IntegerField()
    connection = models.CharField(max_length=255)
    interfaces= models.CharField(max_length=255)
    battery = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    frontCamera= models.CharField(max_length=255)
    rearCamera = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255)
    
    class Meta:
        db_table= 'mobile'

    