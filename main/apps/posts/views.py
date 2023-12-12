#from django.views.generic import templateView
from django.shortcuts import render
from .models import Post
#VISTA BASADAS EN FUNCIONES 
def posts(request):
    posts= Post.objects.all()
    return render(request, 'post/posts.html', {'posts' : posts})
    #, request.FILES

'''
class IndexView(templateView):
        template_name ='index.html'
    
    
    #def get(delf, request):
        #return render(request, 'index.html')'''