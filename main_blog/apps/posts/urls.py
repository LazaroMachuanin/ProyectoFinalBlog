from django.urls import path
from .views import *
# PostListView, PostDetailView,PostCreateView, CategoriaCreateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'apps.posts'

urlpatterns = [
    path("posts/", PostListView.as_view(), name='posts'),
    path("posts/<int:id>/", PostDetailView.as_view(), name='post_individual'),
    path('posts/crear', PostCreateView.as_view(), name='crear_post'), #Crear un post
    #path('posts/', PostCreateView.as_view(), name='crear_post'), #Crear un post
    path('posts/categoria', CategoriaCreateView.as_view(), name='crear_categoria'),
    #path('posts/lista_categoria', CategoriaListView.as_view(), name='lista_categoria'),
    path('categoria/lista_categoria', CategoriaListView.as_view(), name='lista_categoria'),
    path('categoria/<int:pk>/delete/', CategoriaDeleteView.as_view(), name='eliminar_categoria'),
    path('posts/<int:pk>/modificar_post/', PostUpdateView.as_view(), name='modificar_post'),#Modificar un artículo
    path('posts/<int:pk>/eliminar/', PostDeleteView.as_view(), name='eliminar_post'),#Eliminar un artículo
    path('categoria/<int:pk>/post_por_categoria/', PostPorCategoriaView.as_view(), name='post_por_categoria'),
    #path('posts/<int:id>', ArticuloDetailView.as_view(), name="posts_detalle"),#Ver un artículo individual
]

#path('categoria/<int:pk>/articulos/', ArticuloPorCategoriaView.as_view(), name='articulos_por_categoria'),
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
