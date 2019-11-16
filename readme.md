# [Criando poderosas API's RESTful com Django Rest Framework](www.udemy.com/course/apis-restful-com-django-rest-framework/)
_requirements: django, djangorestframework, pillow, django-filter_

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
* GET - Recuperar um recurso
* POST - Criar um novo recurso
* PATCH - Atualizar parte de um recurso
* PUT - Atualizar o estado de um recurso
* DELETE - Remover um recurso existente

##### SERIALIZER
É responsavel por retornar um objeto em **JSON**, no caso, de acordo com o modelo passado na classe implementada.

##### VIEWSET
O ViewSet irá realizar uma ação a partir do serializer especificado na classe. As ViewSets criadas serão encaminhadas para rotas do DRF,
e serão incluidas em um URL do Django, assim como as Views defaults do Django são implementadas. A diferença é que o próprio DRF irá criar
as subURLs, com o ID, e a ação utilizada na ViewSet. Esta ação de criar subURLs vem implementada na classe 'register' do módulo 'routers'.

##### URLs
Dependendo da ViewSet, o DRF já possui por padrão um template, seja a requisição um GET, POST, DELETE, etc. Se uma ViewSet requisitar uma listagem
de todos objetos de um model (tabela do banco de dados), o template gerado pelo DRF irá conter a listagem dos objetos em JSON com os campos especificados no serializer, e também um form para realizar a requisição POST com os mesmos campos. Também é possível obter o objeto puro de JSON para uma id desejada.

O DRF já possui o CRUD implementado em seu código-base, por isso quando se entra em um objeto criado no banco de dados, é possível dar um UPDATE neste objeto, e, então, modificando seus dados. Além disso, é possível deletar este mesmo objeto. Ou seja, o CRUD completo fornecido pelo DRF com poucas linhas de código.

O CRUD é implementado pelo herança do 'ModelViewSet', ou seja, se uma ViewSet for criada com heraça com esta classe, o CRUD vai estar disponível.

##### MÉTODOS DEFAULT
Por default, a classe ModelViewSet oriunda do DRF possui alguns métodos atrelados, e todos são passíveis de mudanças pelo dev ao realizar polimorfismo, além de todos ter como argumento o request, *args e **kwargs. Segue a lista abaixo:
* list() - Quando o request mandado para o site é o **GET**, este método é acionado, e assim, mostra todos os objetos do model em questão. OBS: Este método só é acionado pelo **GET** quando é preterível ver todos os objetos do endpoint.
* create() - Acionado quando o server requisita a ação **POST**.
* destroy() - Acionado quando o server requisita a ação **DELETE** de um objeto, e não de um endpoint em sua totalidade.
* update() - Acionado quando o server requisita a ação **PUT** de um objeto por inteiro, ou seja, este objeto deve ser retonado por completo, mesmo que a alteração tenha sido em apenas um dos campos do objeto.
* partial_update() - Acionado quando o server requisita a ação **PATCH**, ou seja, ao contrário da ação _PUT_, não é necessário retornar o objeto por completo, e sim, apenas os campos que estão sendo modificados.
* retrieve() - Comportamento parecido com o do _list()_, acionado quando ação é o **GET**, porém, ao contrário do método já mencionado, este método é acionado quando é desejado ver apenas um objeto do endpoint.

OBS: O _request_ repassado como argumento nas funções possui uma coleção de dados implícitos, inclusive o _request.data_, que é um dicionário, traduzido de um objeto JSON automaticamente, em que possui todas as informações do objeto em questão. Isto é válidos para todos os verbos, menos para o _GET_, pois este não retorna o objeto JSON

###### MÉTODOS PRÓPRIOS
É possível criar próprios métodos, além dos métodos default. Para isso, é necessário realizar o comando `import rest_framework.decorators.action`, em que será importado o decorator **action** do Django, em que este decorator possui alguns argumentos, entre eles o _methods_, que recebe os verbos que acionam este método, e o _detail_ que recebe True se a ação é em um recurso (objeto) do endpoint, ou False se a ação será feita no endpoint. Caso _detail_ possua o valor de True, é necessário colocar o argumento _pk_ no método, e não no decorator.

Para acessar a URL desta nova action: *host/endpoint/id/action* (Se for em cima de um recurso, e não de um endpoint)

Ver *pontos_turisticos -> api -> viewsets*

##### FILTROS
É possível realizar filtros dos objetos dos endpoints de diversas maneiras, entre elas estão:

* get_queryset(self): Com este filtro, é possível realizar buscas manuais por caracteristicas desejadas. O request passado para o método possui um atributo chamado *query_params*, e neste possui as características que foram buscadas pelo usuário ou server.
    * Ver: *pontos_turisticos -> api -> viewsets: get_querysets*
* DjangoFilter: É uma biblioteca a parte que se comunica com o DRF e Django que permite filtros mais rebuscados e de forma bem simples. Para realizar a filtragem, é necessário colocar dentro da viewset da aplicação desejada, a variável *filter_fields* e atribuir um iterável com os campos que façam parte da filtragem. Com isso, no endpoint da aplicação, irá aparecer um botão **Filter** em que aparecerá os campos para o usuário preencher com as características desejadas.
    * É necessário habilitar o DjangoFilter em **INSTALLED_APPS** colocando *django_filter*
    * Caso queira habilitar a filtragem para todas as aplicações: Ver: *turistic_site -> settings: REST_FRAMEWORK['DEFAULT_FILTER_BACKENDS']*
    * Ver: *atracoes -> api -> viewsets: filter_fields*

#### REST
Um conjunto de regras/constraints em que uma API deve seguir para está dentro dos conformes para um bom funcionamento. Serve como uma espécie
de manual de sobrevivência para uma API.
