from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html') #decorator - mashes up with rango/cats.html
def get_category_list(cat=None): #optional parameter - None fallback value
    return {'cats': Category.objects.all(),
            'act_cat': cat}


