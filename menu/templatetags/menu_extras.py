from django import template
from django.template.loader import render_to_string

from menu.models import MenuItem



register = template.Library()


@register.simple_tag
def menu_list():
    menu = MenuItem.objects.all()
    
    return render_to_string('menu/tags/menu_list.html', {
        'menu': menu,
        })

