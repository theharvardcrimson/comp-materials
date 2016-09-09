from django import template

register = template.Library()


@register.filter()
def excite(val):
    return val.upper()
