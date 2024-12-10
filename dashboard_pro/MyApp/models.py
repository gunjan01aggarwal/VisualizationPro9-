from django.db import models

# Create your models here.
class Data(models.Model):
    end_year=models.CharField(max_length=50,blank=True,null=True)
    intensity=models.IntegerField(blank=True,null=True)
    sector=models.CharField(max_length=300,blank=True,null=True)
    topic=models.CharField(max_length=100,null=True,blank=True)
    insight=models.TextField(null=True,blank=True)
    url=models.TextField(null=True,blank=True)
    region=models.CharField(max_length=200,null=True,blank=True)
    start_year=models.CharField(max_length=50,blank=True,null=True)
    impact=models.CharField(max_length=50,blank=True,null=True)
    added=models.DateTimeField(blank=True,null=True)
    published=models.DateTimeField(blank=True,null=True)
    country=models.CharField(max_length=200,null=True,blank=True)
    relevance=models.IntegerField(null=True,blank=True)
    pestle=models.CharField(max_length=200,blank=True,null=True)
    source=models.TextField(blank=True,null=True)
    title=models.TextField(null=True,blank=True)
    likelihood=models.IntegerField(null=True,blank=True)


