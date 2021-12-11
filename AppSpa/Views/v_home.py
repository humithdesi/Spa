from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request,'AppSpa/home.html')
def error(request, exception):
    return render(request, 'AppSpa/Erro.html',{'loi':exception})