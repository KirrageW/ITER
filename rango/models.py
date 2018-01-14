from django.db import models

# Create your models here. edited 5.3 creating models
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True) #every category must be unique

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0) #page will start with 0 views

    def __str__(self):
        return self.title

    
