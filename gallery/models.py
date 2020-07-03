from django.db import models
from datetime import date

# Create your models here.

class Sitecolor(models.Model):
    name = models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.name


class Sitecategory(models.Model):
    name = models.CharField(max_length=32, unique=True)
    def __str__(self):
        return self.name


class Website(models.Model):
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField(default="", unique=True)
    img_pc = models.ImageField(upload_to='images_pc/', default='')
    img_sm = models.ImageField(upload_to='imges_sm/', default='')
    add_date = models.DateField(default=date.today)
    color = models.ManyToManyField(Sitecolor)
    category = models.ManyToManyField(Sitecategory)
    def __str__(self):
        return self.name
