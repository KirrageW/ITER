from django.db import models

# Create your models here. edited 5.3 creating models
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True) #every category must be unique
    views = models.IntegerField(default=0) #chapter 5 exercise - add views
    likes = models.IntegerField(default=0) #add likes. both with default 0
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0) #page will start with 0 views

    def __str__(self):
        return self.title

    
