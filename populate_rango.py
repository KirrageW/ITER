import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup() #imports our Django project's settings from settings.py
from rango.models import Category, Page

def populate():
    #create lists of dictionaries with pages for categories
    #then dictionary of dictionaries for categories
    #allows iteration through data, and adding data to models

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http//docs.python.org/2/tutorial/"},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/"}]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https:docs.djangoproject.com/en/1.9/intro.tutorial01/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"}]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"} ]

    cats =  {"Python": {"pages": python_pages},
             "Django": {"pages": django_pages},
             "Other Frameworks": {"pages": other_pages}}

    #next code goes through cats dictionary, adds categories, adds pages
    for cat, cat_data in cats.items():
        c = add_cat(cat) #temporary local variable because Page requires a Category reference
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    #prints categories that are now added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-{0} - {1}".format(str(c), str(p))) #will print names on terminal

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0] #get_or_create checks for already existing versions
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

#start exectuion here
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
    

        
