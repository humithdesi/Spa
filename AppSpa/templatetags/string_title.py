from django import template


register=template.Library()

register.filter(name='title')
def Title(value):
    title=value.title()
    return title