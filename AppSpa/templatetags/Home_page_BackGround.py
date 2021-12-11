from django import template
from ..Models.m_post import Tag,Post

register=template.Library()

@register.inclusion_tag('AppSpa/HomeBackGround/Background.html',)
def HomeBackGround():
    content={}
    return content
@register.inclusion_tag('AppSpa/HomeBackGround/MoTaCongNghe.html',)
def MoTaCongNghe():
    content={}
    return content
@register.inclusion_tag('AppSpa/HomeBackGround/Foorter.html',)
def Foorter():
    tags=Tag.objects.all()
    posts = Post.objects.all()
    content={'tags':tags,'posts':posts}
    return content