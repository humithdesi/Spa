from django.shortcuts import render
from django.http import HttpResponse,Http404
from ..Models.m_post import Post,Tag
# Create your views here.
def PostPage(request,slug):
    try:

        post=Post.objects.get(slug=slug)
        posts=Post.objects.all()[:6]
        tags=Tag.objects.all()
        content={'post':post,'posts':posts,'tags':tags}
        return render(request,'AppSpa/Post.html',content)

    except Post.DoesNotExist:
            raise Http404("Bài viết không tồn tại")