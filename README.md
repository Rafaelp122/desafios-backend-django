# 5 Desafios de Backend com Django REST Framework

Este repositório contém as minhas soluções para 5 desafios práticos de backend, focados na construção de APIs RESTful utilizando Django e Django REST Framework (DRF).

O objetivo é praticar e demonstrar conceitos fundamentais e avançados, desde um CRUD básico até autenticação, relacionamentos e permissões personalizadas.

Cada desafio está em sua própria pasta e é um **projeto Django completamente independente**, com seu próprio banco de dados, mas todos compartilham as mesmas dependências definidas no `requirements.txt` da raiz.

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Django**
* **Django REST Framework (DRF)**
* **SQLite** (banco de dados padrão do Django)
* **Git & GitHub**

---

## 🚀 Os Desafios

Aqui está um índice de todos os desafios e os principais conceitos praticados em cada um:

### 1. [API de Lista de Tarefas](./desafio-01-api-tarefas/)
* **Objetivo:** Criar um CRUD (Create, Read, Update, Delete) simples para gerenciar uma lista de tarefas (To-Do).
* **Conceitos:** `Models`, `Serializers` (`ModelSerializer`), `ViewSets` (`ModelViewSet`) e `DefaultRouter`.

### 2. [API de Produtos com Filtro](./desafio-02-api-produtos/)
* **Objetivo:** Criar uma API para cadastrar produtos e permitir filtros por categoria via *query params* (ex: `/api/produtos/?categoria=Eletrônicos`).
* **Conceitos:** Views genéricas (`ListCreateAPIView`), sobrescrever o método `get_queryset()` e `request.query_params`.

### 3. [API de Usuários com Autenticação](./desafio-03-api-usuarios/)
* **Objetivo:** Implementar um sistema de registo (cadastro) e login (autenticação) usando o `User` model padrão do Django.
* **Conceitos:** Autenticação (`TokenAuthentication`), `rest_framework.authtoken` (view `obtain_auth_token`), `UserSerializer` com `create_user()` (para hashing de senha) e Permissões (`IsAuthenticated`, `AllowAny`).

### 4. [API de Chamados com Relacionamentos](./desafio-04-api-chamados/)
* **Objetivo:** Criar uma API para gerenciar chamados de suporte, onde cada chamado pertence a um usuário (Relação Um-para-Muitos).
* **Conceitos:** Relacionamentos (`ForeignKey`), rotas aninhadas (ex: `/usuarios/<id>/chamados/`) e sobrescrever `perform_create()` para ligar o chamado ao usuário da URL.

### 5. API Avançada de Biblioteca (Ainda não iniciado)
* **Objetivo:** Uma API completa com autenticação, múltiplos relacionamentos (`ForeignKey`, `ManyToManyField`) e permissões de nível de objeto (ex: um usuário só pode ver os *seus próprios* empréstimos).
* **Conceitos:** Permissões personalizadas (`BasePermission`), múltiplos modelos e filtros complexos.

---

## 🏃 Como Executar

A instalação é centralizada. Você instala as dependências uma vez na raiz do repositório e pode executar qualquer um dos 5 projetos.

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/Rafaelp122/desafios-backend-django.git](https://github.com/Rafaelp122/desafios-backend-django.git)
    cd desafios-backend-django
    ```

2.  **Crie e ative um ambiente virtual:**
    (Você pode criar este `venv` aqui mesmo na pasta raiz)
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências (da raiz):**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Escolha um desafio e execute:**
    * Navegue até a pasta do desafio (ex: `cd desafio-01-api-tarefas`).
    * Rode as migrações: `python manage.py migrate`
    * Inicie o servidor: `python manage.py runserver`
    * Para rodar outro desafio, pare o servidor (`Ctrl+C`), vá para a outra pasta (`cd ../desafio-02-api-produtos`) e repita (`python manage.py runserver`).