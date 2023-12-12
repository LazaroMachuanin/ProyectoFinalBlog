from django.urls import path
from .views import posts
#from django.conf import settings
#from django.conf.urls.static import static


app_name='apps.posts'

urlpatterns = [
    path('posts/', posts, name = 'posts'),
    #return render(request, 'posts.html')

    
    #pass
    
]


#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)