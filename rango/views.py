from django.shortcuts import render

from django.http import HttpResponse
from rango.models import Category

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



