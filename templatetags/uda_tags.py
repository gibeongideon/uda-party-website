from django import template
from home.models import Advert

register = template.Library()



# Advert snippets
@register.inclusion_tag('home/home_page.html', takes_context=True)
def adverts(context):
    return {
        'adverts': Advert.objects.all(),
        'request': context['request'],
    }
