from django.shortcuts import render
from django.http import HttpResponse,Http404
from ..Models.m_post import Tag
from ..Models.m_post import Post
# Create your views here.
def TagList(request,slug):
    try:
        tag=Tag.objects.get(slug=slug)
        posts=Post.objects.all().filter(tag__slug=slug)
        content={'tag':tag,'posts':posts}
        return render(request,'AppSpa/tag_list.html',content)
    except Tag.DoesNotExist:
        raise Http404("Bài viết không tồn tại")