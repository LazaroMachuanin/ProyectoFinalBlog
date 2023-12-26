from django.views.generic import TemplateView # est es B va con B
#from django.views import View # esto es A y va con A
from django.shortcuts import render
#from django.http import HttpResponseNotFound

class IndexView(TemplateView):
    template_name = 'index.html'   #esto es B
    
    
# class indexview(View):
#     def get(self, request):
#         return render(request,'index.html') # con clases y return A
    

#def index(request):
#    return render(request, 'index.html')

#def pagina_404(request, exception):
    #return HttpResponseNotFound('<h1>Pagina no encontrada</h1>')

def about(request):
    return render(request, 'about.html')

def registro(request):
    return render(request, 'registro.html')

def home(request):
    return render(request, 'home.html')

