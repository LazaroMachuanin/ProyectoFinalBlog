from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView

app_name = 'apps.posts'

urlpatterns = [
    path("posts/", PostListView.as_view(), name='posts'),
    path("posts/<int:id>/", PostDetailView.as_view(), name='post_individual'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)