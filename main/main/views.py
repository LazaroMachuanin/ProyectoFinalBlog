#from django.views.generic import templateView
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

#def posts(request):
#    return render(request, 'posts.html')

'''
class IndexView(templateView):
        template_name ='index.html'
    
    
    #def get(delf, request):
        #return render(request, 'index.html')'''