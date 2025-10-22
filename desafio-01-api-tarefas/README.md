# Desafio 1: API de Lista de Tarefas (To-Do)

Este projeto é a solução para o primeiro desafio de Django REST Framework, focado em criar um CRUD básico para gerenciar tarefas.

## 🎯 Objetivo

Criar uma API simples que gerencie tarefas (to-do list) com Django REST Framework.

## 📋 Instruções do Desafio

1.  Crie um projeto Django chamado `tarefas_api`.
2.  Crie um app chamado `tarefas`.
3.  No app `tarefas`, crie um model `Tarefa` com os campos:
    * `titulo` (CharField)
    * `descricao` (TextField)
    * `concluida` (BooleanField, default=False)
4.  Crie serializers, views e rotas para permitir:
    * Listar todas as tarefas
    * Criar uma nova tarefa
    * Editar e excluir tarefas
5.  Teste os endpoints no navegador ou no Postman.

## 🚀 Como Executar o Projeto

1.  **Clone o repositório** (se ainda não o fez):
    ```bash
    git clone [https://github.com/Rafaelp122/desafios-backend-django.git](https://github.com/Rafaelp122/desafios-backend-django.git)
    cd desafios-backend-django/desafio-01-api-tarefas
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    *(Você pode criar um `requirements.txt` para este projeto com `pip freeze > requirements.txt`)*
    ```bash
    pip install django djangorestframework
    ```

4.  **Rode as migrações:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```

## 🌐 Endpoints da API

* **Listar e Criar Tarefas:**
    * `GET /api/tarefas/`
    * `POST /api/tarefas/`
* **Detalhar, Atualizar e Deletar Tarefa:**
    * `GET /api/tarefas/<id>/`
    * `PUT /api/tarefas/<id>/`
    * `PATCH /api/tarefas/<id>/`
    * `DELETE /api/tarefas/<id>/`
