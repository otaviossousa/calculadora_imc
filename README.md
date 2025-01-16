# Calculadora IMC

Este projeto é uma aplicação Django para calcular o Índice de Massa Corporal (IMC).

## Funcionalidades

- Entrada de dados do usuário (peso e altura)
- Cálculo do IMC
- Exibição do resultado do IMC com a classificação correspondente

## Como usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/otaviossousa/calculadora_imc.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd calculadora_imc
    ```
3. Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
4. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
5. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:8000
    ```

## Estrutura do Projeto

- `calculadora_imc/`: Diretório principal do projeto Django.
- `imc/`: Aplicação Django que contém a lógica de cálculo do IMC.
- `templates/`: Arquivos HTML para renderização das páginas.
- `static/`: Arquivos estáticos (CSS).
