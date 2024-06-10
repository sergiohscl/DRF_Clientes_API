# Projeto DRF_Clientes_API
## Objetivo do projeto implementar conceitos do DRF:
### validações;
### paginação;
### buscas, filtros;
### deploy na aws;

<hr>

## Documentação do django
https://www.djangoproject.com/

## Documentação django-rest-framework paginação
https://www.django-rest-framework.org/api-guide/pagination/

## Documentação django-rest-framework filter
https://www.django-rest-framework.org/api-guide/filtering/

## Instalando ambiente virtual
    python3 -m venv venv

## Ativando e desativando ambiente virtual
### Linux
    . venv/bin/activate
    deactivate

### Windows
    source venv\Scripts\Activate.ps1   # terminal powersheel        
    source venv\Scripts\Activate.bat   # terminal cmd

## Instalando django no ambiente virtual
    pip install django

## Iniciando project django
    django-admin startproject <nome-project> .

## Instale as dependências no projeto
    pip install -r requirements.txt

## Migrando a base de dados do Django
    python manage.py makemigrations
    python manage.py migrate

## Criando e modificando a senha de um super usuário
    python manage.py createsuperuser

## Rodando django-admin
    python manage.py runserver