from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Autor, Categoria
# Create your views here.
def listar_livros(request):
    if request.method == 'GET':
        livros = Livro.objects.select_related('autor', 'categoria').all()
        return render(request, 'Livro/listar.html', {'livros': livros})

def adicionar_livro(request):
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor_id = request.POST.get('autor')
        categoria_id = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        imagem = request.FILES.get('imagem')  # pega o arquivo enviado

        autor = get_object_or_404(Autor, id=autor_id)
        categoria = get_object_or_404(Categoria, id=categoria_id)

        Livro.objects.create(
            titulo=titulo,
            autor=autor,
            categoria=categoria,
            descricao=descricao,
            imagem=imagem
        )

        return redirect('lista_livros')  # volta para a página de listagem

    return render(request, 'Livro/adicionar_livro.html', {
        'autores': autores,
        'categorias': categorias
    })
    
def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        livro.titulo = request.POST.get('titulo')
        autor_id = request.POST.get('autor')
        categoria_id = request.POST.get('categoria')
        livro.descricao = request.POST.get('descricao')
        imagem = request.FILES.get('imagem')

        livro.autor = get_object_or_404(Autor, id=autor_id)
        livro.categoria = get_object_or_404(Categoria, id=categoria_id)

        if imagem:
            livro.imagem = imagem  # só atualiza se houver upload novo

        livro.save()
        return redirect('lista_livros')

    return render(request, 'Livro/editar_livro.html', {
        'livro': livro,
        'autores': autores,
        'categorias': categorias
    })
    
def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)

    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')

    return render(request, 'Livro/deletar_livro.html', {'livro': livro})