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

1.  **Pré-requisitos:** Certifique-se de que você já ativou seu ambiente virtual e instalou as dependências do arquivo `requirements.txt` na **raiz** do repositório.
    ```bash
    # (Na pasta raiz do repositório)
    # source venv/bin/activate
    # pip install -r requirements.txt
    ```

2.  **Navegue até esta pasta do desafio:**
    ```bash
    # (Estando na raiz)
    cd desafio-03-api-usuarios
    ```

3.  **Rode as migrações:**
    *(Este passo é crucial para criar as tabelas do User e do Token)*
    ```bash
    python manage.py migrate
    ```

4.  **Inicie o servidor:**
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