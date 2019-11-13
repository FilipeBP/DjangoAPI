# [Criando poderosas API's RESTful com Django Rest Framework] (https://www.udemy.com/course/apis-restful-com-django-rest-framework/)
_requirements: django, djangorestframework_

## Do que o curso se trata?
O Django Rest Framework utiliza-se do framework bastante conhecido, o Django (sim, são diferentes), para que haja a aplicação da API juntamente
com todas a funcionalidades do framework Django.

## Fluxo do aplicativo
![Fluxo](FluxoAPP.png)

### Passos a ser seguidos
* Procedimento normal de um início de projeto Django
    * Cria uma venv
    * Pip install requirements
    * django-admin startproject nome_do_projeto .
    * python manage.py makemigrations
    * python manage.py migrate
* Adiciona-se o Django Rest nos aplicativos permitidos
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### Esclarecendo alguns conceitos
#### API
Uma API é uma interface que se comunica com um aplicativo, seja ele web, seja ele desktop, ou até mobile, e retorna a ação requisitada pelo usuário.
É a interface interlocutora entre a aplicação e o usuário, realizando este intermédio. Emprega-se da serialização para realizar estes verbos. A linguagem utilizada para isto é o **JSON**.

Os verbos mencionados acima são:
* GET
* POST
* PATCH
* PUT
* DELETE

#### REST
Um conjunto de regras/constraints em que uma API deve seguir para está dentro dos conformes para um bom funcionamento. Serve como uma espécie
de manual de sobrevivência para uma API.
