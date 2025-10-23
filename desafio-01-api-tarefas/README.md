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

1.  **Pré-requisitos:** Certifique-se de que você já ativou seu ambiente virtual e instalou as dependências do arquivo `requirements.txt` na **raiz** do repositório.
    ```bash
    # (Na pasta raiz do repositório)
    # source venv/bin/activate
    # pip install -r requirements.txt
    ```

2.  **Navegue até esta pasta do desafio:**
    ```bash
    # (Estando na raiz)
    cd desafio-01-api-tarefas
    ```

3.  **Rode as migrações:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Inicie o servidor:**
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