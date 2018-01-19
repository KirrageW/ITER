from django.db import models
from django.template.defaultfilters import slugify

# Create your models here. edited 5.3 creating models
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True) #every category must be unique
    views = models.IntegerField(default=0) #chapter 5 exercise - add views
    likes = models.IntegerField(default=0) #add likes. both with default 0
    slug = models.SlugField(unique=True) #chapter 6.3 making good urls

    #override save method
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'categories' #capital letter on categories??

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0) #page will start with 0 views

    def __str__(self):
        return self.title

    
