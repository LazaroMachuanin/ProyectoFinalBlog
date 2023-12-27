from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.



#Categoria

#def default_image():
#    return 'media/default_category_image.png'  # Ruta a tu imagen por defecto

class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    descripcion = models.TextField(null=False, default='sin descripcion')
    imagen = models.ImageField(upload_to='media', null=True, blank=True, default='static/post_default.png')
    texto =models.DateTimeField(default=timezone.now)
    #imagen = models.ImageField(upload_to='media', null=True, blank=True, default=default_image)
    #imagen = models.ImageField(null=True, blank=True, upload_to='media', default='media/post_default.png')



    def __str__(self):
        return self.nombre

#Post  
class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin Categoria')
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.png')
    publicado =models.DateTimeField(default=timezone.now)

    
    class Meta:
        ordering = ('-publicado',)
    
    def __str__(self):
        return self.titulo

    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()

#Comentarios
class Comentario(models.Model):
    posts = models.ForeignKey('posts.Post', on_delete = models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.texto