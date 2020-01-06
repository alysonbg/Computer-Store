[![Build Status](https://travis-ci.org/alysonbg/Computer-Store.svg?branch=master)](https://travis-ci.org/alysonbg/Computer-Store)

## Api que simula uma loja de computadores

### Para rodar o projeto sigua as instruções:
1. Clone o repositorio 
2. Crie um virtualenv
3. Rode o comando pip install -r requirements.txt
4. Crie um arquivo .env com as seguintes variaveis de ambiente:

Ex:

- SECRET_KEY=123
- ALLOWED_HOSTS=127.0.0.1, .localhost

Obs: As variaveis nao devem conter nenhum tipo de aspas

5. Rodar o comando python manage.py migrate
6. Rodar o comando python manage.py runserver