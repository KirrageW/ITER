from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),#removed  url(r'^$', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', #note parameter name in url pattern - need to declare in view
        views.show_category, name='show_category'), #\w for alphanumeric chars, \- for hypens. []+ means match as many as like
    ]
#all view functions in django apps must take a parameter - typicalyl called request. gives access to info frelated to given http request made by user
# for urls - need an additional named parameter for the signature for the given view, too
