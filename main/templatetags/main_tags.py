from django import template
from main.models import NavBar, About, Contact, Service, Offer, Menu, MenuType

register = template.Library()


@register.simple_tag()
def get_nav():
    return NavBar.objects.order_by('order')


@register.inclusion_tag('inc/_nav.html')
def get_nav_bar():
    navbar = get_nav()
    return {'navbar': navbar, }


@register.simple_tag()
def get_about():
    return About.objects.all().first()


@register.simple_tag()
def get_contact():
    return Contact.objects.all().first()


@register.simple_tag()
def get_services():
    return Service.objects.all()


@register.simple_tag()
def get_offer():
    return Offer.objects.filter(enable=True).first()


@register.simple_tag()
def get_menu():
    menu = {}
    for menu_type in MenuType.objects.all():
        menu[menu_type] = Menu.objects.filter(type__exact=menu_type)[:3]
    return menu
