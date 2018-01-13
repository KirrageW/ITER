from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #some kind of dictionary that defines template things - template variable called boldmessage
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    #returns response to client, render function takes user input, template
    #filename amd context dictionary - mash with template to form full html page...
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage2': "I do hope this works"}
    return render(request, 'rango/about.html', context=context_dict)



