from django.views.generic import TemplateView # est es B va con B
#from django.views import View # esto es A y va con A
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = 'index.html'   #esto es B
    
    
# class indexview(View):
#     def get(self, request):
#         return render(request,'index.html') # con clases y return A
    

# def index(request):
#     return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def registro(request):
    return render(request, 'registro.html')

def home(request):
    return render(request, 'home.html')

