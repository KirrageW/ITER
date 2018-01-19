from django.shortcuts import render

from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    #some kind of dictionary that defines template things - template variable called boldmessage
    #chapter 6 - query db for list of all categories, order by number of likes (desc)
    #then retreive top 5 only. place list in context_dict dictionary (which is passed
    #to template engine
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    
    #returns response to client, render function takes user input, template
    #filename amd context dictionary - mash with template to form full html page...
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage2': "I do hope this works"}
    return render(request, 'rango/about.html', context=context_dict)

#6.3 making category pages accessible via slugs 
def show_category(request, category_name_url):
    #create context dictionary as per - gets passed to template renderer eng.
    context_dict = {}

    try:
        #find category slu with given name
        #if no - get() method raises exception
        #if yes - get() method returns one model
        category = Category.objects.get(slug=category_name_slug)

        #retrieve all associated pages
        #filter() returns list pf page objects or raises exception
        pages = Page.objects.filter(category=category)

        #adds our results list to template context under name pages
        context_dict['pages'] = pages
        #we also add category object from
        #database to context dictionary
        #used in template to verify category
        context_dict['category'] = category
    except Category.DoesNotExist:
        #catches exceptions - no category found
        #template display no category message
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)

#basically - define context dictionary,
#           - extract data from models, or catch exceptions
#           - add relevant data to context dicitonary
#           - which category, determined by using value passed
#               in parameter category_name_slug to the show_category() view
#               function
#           - if this category slug is found in category model, we pull associated pages, and
#               add to context_dict
    
    



