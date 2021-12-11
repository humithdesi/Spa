from django import template
from ..Models.m_post import Tag


register=template.Library()

@register.inclusion_tag('AppSpa/background_top.html',)
def Background_top():
    content={}
    return content
@register.inclusion_tag('AppSpa/menu.html',)
def Menu():
    tags=Tag.objects.all()
    content={'tags':tags}
    return content