from django import template
from .. import models


register = template.Library()


@register.simple_tag
def get_site_settings():
    return models.SiteSettings.get_solo()


@register.simple_tag
def get_excursion_list():
    return models.Excursion.objects.all()
