from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.listar_livros, name='lista_livros'),
    path('adicionar_livro/', views.adicionar_livro, name="adicionar_livro"),
    path('editar_livro/<int:pk>/', views.editar_livro, name="editar_livro"),
    path('deletar_livro/<int:pk>/', views.deletar_livro, name="deletar_livro"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)