from django.shortcuts import redirect 
from django.views.generic import ListView, DetailView, CreateView, DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comentario, Categoria
from .forms import ComentarioForm, NuevaCategoriaForm,CrearPostForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import render
from .models import Categoria

#post
class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

#post individual
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(posts_id=self.kwargs['id'])
        return context
    
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.posts_id = self.kwargs['id']
            comentario.save()
            return redirect('apps.posts:post_individual', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/agregarComentario.html'
    success_url = 'comentario/comentarios/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.posts_id = self.kwargs['id']
        return super().form_valid(form)

#Post creación
class PostCreateView(LoginRequiredMixin, CreateView):
        model = Post
        form_class = CrearPostForm
        template_name= 'posts/crear_post.html'
        #success_url= reverse_lazy('apps.posts:posts')
        
        #def vista_dondevas(request):
        #    mostrar_enlace = False
            ########return render(request, 'tu_plantilla.html', {'mostrar_enlace': mostrar_enlace, ...otras_variables_de_contexto})
        #   return render(request, 'posts.html', {'posts': mostrar_enlace})

        def get_success_url(self):
            messages.success(self.request, '¡Post creado con éxito!')
            return reverse_lazy('apps.posts:posts')
        
        #def form_valid(self, form):
        #    form.instance.usuario = self.request.user
        #form.instance.posts_id = self.kwargs['posts_id']
        #    return super().form_valid(form)

        
class PostPorCategoriaView(ListView):
    model = Post
    template_name = 'posts/post_por_categoria.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.filter(categoria_id=self.kwargs['pk'])
        return posts


        
#Categorías
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'posts/crear_categoria.html'

    def get_success_url(self):
        messages.success(self.request, '¡Categoría creada con éxito!')
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            #return reverse_lazy('apps.posts:post')
            return reverse_lazy('apps.posts:crear_post')
        
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'posts/lista_categoria.html'
    context_object_name = 'categorias'  # Cambiado a plural para mantener consistencia

    def get_queryset(self):
        return Categoria.objects.all

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'posts/eliminar_categoria.html'
    success_url = reverse_lazy('apps.posts:lista_categoria')

#Post modificación
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = CrearPostForm
    template_name = 'posts/modificar_post.html'

    def get_success_url(self):
            messages.success(self.request, '¡Post modificado con éxito!')
            return reverse_lazy('apps.posts:posts')


#Post borrar
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/eliminar_post.html'

    def get_success_url(self):
        messages.success(self.request, '¡Borrado con éxito!')
        return reverse_lazy('apps.posts:posts')





'''
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'post/crear_categoria.html'
    success_url = 'categoria/nueva_categoria/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.posts_id = self.kwargs['id']
        return super().form_valid(form)
'''
'''
from typing import Any
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comentario
from django.shortcuts import redirect
from .forms import ComentarioForm

# Vista basada en funciones
# def posts(request):
#     posts = Post.objects.all()
#     return render(request, 'posts.html', {'posts' : posts})

#Vista basada en clases para la lista de posts

class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    
# Vista basada en clases para posts individual 

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = "id"
    queryset =Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(posts_id= self.kwargs['id'])
        super().get_context_data(**kwargs)
        return context
    
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.Post)
        if form.is_valid():
            Comentario.usuario= request.user
            Comentario.posts_id = self.kwargs['id']
            Comentario.save()
            return redirect('apps.posts:post_individual', id = self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
        
class ComentarioCreateView(LoginRequiredMixin, CreateView):
        model = Comentario
        form_class =ComentarioForm
        template_name= 'comentario/agregarComentario.html'
        success_url= 'comentario/comentarios/'

        def form_valid(self, form):
            form.instance.usuario = self.request.user
            form.instance.posts_id = self.kwargs['posts_id']
            return super().form_valid(form)
'''


