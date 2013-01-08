from datetime import datetime
from django.db import models


class ScanPath(models.Model):
    path = models.CharField(max_length=256)


class Photo(models.Model):
    root       = models.ForeignKey(ScanPath)
    path       = models.CharField(max_length=256)
    date_taken = models.DateTimeField(default=datetime(year=1970, month=1, day=1))
    width      = models.IntegerField(blank=True, null=True)
    height     = models.IntegerField(blank=True, null=True)
    make       = models.CharField(max_length=128, blank=True)
    model      = models.CharField(max_length=128, blank=True)
    latitude   = models.FloatField(blank=True, null=True)
    longitude  = models.FloatField(blank=True, null=True)
