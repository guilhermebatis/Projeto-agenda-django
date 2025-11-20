# 🗂️ Agenda em Django

Um projeto de Agenda desenvolvido com **Django**, permitindo criar, editar, visualizar e excluir contatos.  
Ideal para estudos, portfólio e como base para aplicações maiores.

---

## 🚀 Funcionalidades

- ✔️ Cadastro de contatos  
- ✔️ Pesquisa por nome ou sobrenome  
- ✔️ Visualização detalhada de cada contato  
- ✔️ Edição de contatos  
- ✔️ Exclusão de contatos  
- ✔️ Upload de fotos
- ✔️ Interface simples e funcional  

---

## 🏗️ Tecnologias usadas

- **Python 3.10+**
- **Django 4+**
- **HTML / CSS / Bootstrap**
- **SQLite3** (banco local para desenvolvimento)


# Como rodar o projeto

1. Clone o repositório:
   git clone https://github.com/guilhermebatis/Projeto-agenda-django
   cd Projeto-agenda-django

3. Crie um ambiente virtual:
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

4. Instale as dependências:
   pip install -r requirements.txt

5. Faça as migrações:
   python manage.py migrate

6. Inicie o servidor:
   python manage.py runserver
