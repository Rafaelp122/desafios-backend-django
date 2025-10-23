# Desafio 3: API de Usuários com Autenticação

Este projeto é a solução para o terceiro desafio de Django REST Framework, focado em implementar um sistema completo de registo (cadastro), login (autenticação por Token) e listagem de utilizadores protegida.

## 🎯 Objetivo

Criar uma API para cadastrar e autenticar usuários usando o sistema de autenticação padrão do Django.

## 📋 Instruções do Desafio

1.  Crie um app `usuarios`.
2.  Use o model `User` do Django.
3.  Crie uma rota para listar usuários (somente autenticados).
4.  Configure o login via `TokenAuthentication`.
5.  Teste usando tokens no Postman ou Insomnia.

*(Nota: Para cumprir o objetivo de "cadastrar e autenticar", foram criadas rotas adicionais para `/registrar` e `/login`.)*

## 🚀 Como Executar o Projeto

1.  **Clone o repositório** (se ainda não o fez):
    ```bash
    git clone [https://github.com/Rafaelp122/desafios-backend-django.git](https://github.com/Rafaelp122/desafios-backend-django.git)
    cd desafios-backend-django/desafio-03-api-usuarios
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    *(Recomendado: crie um `requirements.txt` neste projeto com `pip freeze > requirements.txt`)*
    ```bash
    pip install django djangorestframework
    ```

4.  **Rode as migrações:**
    *(Este passo é crucial para criar as tabelas do User e do Token)*
    ```bash
    python manage.py migrate
    ```

5.  **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```

## 🌐 Endpoints da API

A API está configurada para ser acessada a partir do prefixo `/api/`.

* **Registar (Cadastro):**
    * `POST /api/registrar/`
    * **Body (JSON):** `{ "username": "...", "password": "...", "email": "..." }`

* **Login (Obter Token):**
    * `POST /api/login/`
    * **Body (JSON):** `{ "username": "...", "password": "..." }`
    * **Resposta:** `{ "token": "seu_token_aqui_..." }`

* **Listar Usuários (Requer Autenticação):**
    * `GET /api/usuarios/`
    * **Header:** `Authorization: Token seu_token_aqui_...`

## 🔑 Fluxo de Teste (Postman / Insomnia)

Para testar este projeto, siga este fluxo:

1.  **Registe um Usuário:** Faça uma requisição `POST` para `/api/registrar/` com os dados do novo utilizador.
2.  **Faça Login:** Faça uma requisição `POST` para `/api/login/` com o `username` e `password` que acabou de criar.
3.  **Copie o Token:** Copie o valor do `token` que foi retornado na resposta do login.
4.  **Teste a Rota Protegida:** Faça uma requisição `GET` para `/api/usuarios/`.
    * Adicione um *Header* (Cabeçalho) de autorização:
        * **Key:** `Authorization`
        * **Value:** `Token SEU_TOKEN_COPIADO_AQUI`
    * A requisição agora deve funcionar e retornar a lista de utilizadores. Se remover o *Header*, deve receber um erro 401 (Não Autorizado).