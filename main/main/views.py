#from django.views.generic import templateView
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def posts(request):
    return render(request, 'posts.html')

def about(request):
    return render(request, 'about.html')

def registro(request):
    return render(request, 'registro.html')

def home(request):
    return render(request, 'home.html')

'''
class IndexView(templateView):
        template_name ='index.html'
    
    
    #def get(delf, request):
        #return render(request, 'index.html')'''