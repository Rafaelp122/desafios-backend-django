# Desafio 2: API de Produtos com Filtro

Este projeto é a solução para o segundo desafio de Django REST Framework, focado em cadastrar produtos e permitir a filtragem da lista por *query parameters*.

## 🎯 Objetivo

Criar uma API que cadastre produtos e permita filtrar por categoria.

## 📋 Instruções do Desafio

1.  Crie um app `produtos`.
2.  Crie o model `Produto` com:
    * `nome` (CharField)
    * `preco` (FloatField)
    * `categoria` (CharField)
3.  Faça uma rota `/produtos/` com listagem e criação.
4.  Adicione suporte a filtro via query params, ex: `/produtos/?categoria=Eletrônicos`

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
    cd desafio-02-api-produtos
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

A API está configurada para ser acessada a partir do prefixo `/api/`.

* **Listar e Criar Produtos:**
    * `GET /api/produtos/`
    * `POST /api/produtos/`

* **Filtragem por Categoria:**
    * `GET /api/produtos/?categoria=NomeDaCategoria`
    * *Exemplo:* `http://127.0.0.1:8000/api/produtos/?categoria=Eletrônicos`