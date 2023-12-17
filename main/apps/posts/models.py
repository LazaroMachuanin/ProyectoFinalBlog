from django.db import models
import django.db.models.deletion
import django.utils.timezone

#Categoria
class Categoria(models.Model):
    #pass
    #id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    nombre= models.CharField(max_length=30,  null= False)

    def __str__(self):
        return self.nombre

class Post(models.Model):    
    #id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    titulo= models.CharField(max_length=50)
    subtitulo= models.CharField(blank=True, max_length=100, null=True)
    fecha= models.DateTimeField(auto_now_add=True)
    texto= models.TextField()
    activo= models.BooleanField(default=True)
    imagen= models.ImageField(blank=True, default='main/static/post_default.png', null=True, upload_to='media/')
    publicado= models.DateTimeField(default=django.utils.timezone.now)
    categoria= models.ForeignKey(default='sin categoria', null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.categoria')

    def __str__(self):
        return self.titulo

    def delete(self, using=None, keep_parents=False):
            #self.imagen.delete(self.imagen.name)
            #super().delete()
            if self.imagen:
                self.imagen.delete()
                super().delete(using=using, keep_parents=keep_parents)
            pass

class Meta:
        ordering= ('-publicado',)
    # Create your models here.

# Create your models here.
