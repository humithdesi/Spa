from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse,Http404
# Create your views here.
def Home(request):
    try:
        return render(request,'AppSpa/home.html')
    except:
        raise Http404("Trang Không Tồn Tại")

def error(request, exception):
    return render(request, 'AppSpa/Erro.html',{'loi':exception})