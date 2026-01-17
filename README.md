# 📚 Django Biblioteca CRUD

Mini projeto desenvolvido em **Django** para gerenciamento de livros, com funcionalidades de **CRUD** (Criar, Listar, Editar e Deletar).

O sistema permite cadastrar livros com autor, categoria, descrição e imagem, utilizando **Bootstrap** para o layout.

---

## 🚀 Funcionalidades

- 📖 Listar livros
- ➕ Adicionar novo livro
- ✏️ Editar livro existente
- 🗑️ Excluir livro
- 🖼️ Upload de imagem do livro
- 🎨 Interface responsiva com Bootstrap

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Django 6
- SQLite
- Bootstrap 5
- HTML + CSS

---

## ⚙️ Como rodar o projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/django-biblioteca-crud.git
cd django-biblioteca-crud

2️⃣ Criar ambiente virtual (opcional)

python3 -m venv venv
source venv/bin/activate

3️⃣ Instalar dependências

pip install django

4️⃣ Rodar migrações

python manage.py makemigrations
python manage.py migrate

5️⃣ Criar superusuário (opcional)

python manage.py createsuperuser

6️⃣ Iniciar o servidor

python manage.py runserver

Acesse no navegador:

http://127.0.0.1:8000/

🖼️ Upload de imagens

As imagens dos livros são armazenadas na pasta:

media/livros/

Certifique-se de que o MEDIA_URL e MEDIA_ROOT estão configurados no settings.py.
📌 Observações

    Projeto com fins educacionais

    Ideal para quem está aprendendo Django e CRUD

    Código simples e organizado

👨‍💻 Autor

Desenvolvido por bbenito 🚀
Projeto de estudo em Django
