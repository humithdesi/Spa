from django import template
from ..Models.m_post import Post

register=template.Library()

@register.inclusion_tag('AppSpa/PostRight/lienketnhanh_right.html',)
def LienKetNhanh():
    posts = Post.objects.all()
    content = {'posts': posts}
    return content
@register.inclusion_tag('AppSpa/PostRight/dangky_right.html',)
def DangKy():
    content={}
    return content
@register.inclusion_tag('AppSpa/PostRight/tieudiemweb_right.html',)
def TieuDiemWeb():
    posts=Post.objects.all()
    content={'posts':posts}
    return content

