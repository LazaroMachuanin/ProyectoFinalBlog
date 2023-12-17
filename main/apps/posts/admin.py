from django.contrib import admin
# Register your models here.
from .models import Categoria, Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display= ('id','titulo','subtitulo', 'fecha', 'texto', 'activo', 'categoria', 'imagen', 'publicado')
    pass

admin.site.register(Categoria)
# Register your models here.
