# iclinic-challenge: Prescription
Autor: Lucas da Silva de Oliveira (lucasoliveira783@gmail.com, https://www.linkedin.com/in/lucas-sil-oliveira)

## Motivação

Esse é um software desenvolvido para o desafio "iclinic-python-challenge" da empresa iclinic. O programa foi desenvolvido utilizando a linguagem python 3.8.3 juntamente com o framework Django. O framework foi escolhido pois foram encontradas ferramentas como django rest. Além disso, foram utilizadas bibliotecas como requests e request-cache para chamadas externas. Para realização dos testes foi utilizada a pytest.

## Requisitos

- docker (versão recomendada: 19.03)
- docker compose (versão recomendada: 1.27)

## Instalação

```bash
docker-compose build
```

```bash
docker-compose build up
```

```bash
docker-compose exec web python manage.py migrate
```

### Possiveis erros 

Erro: port is already allocated
```bash
ERROR: for web  Cannot start service web: driver failed programming external connectivity on endpoint iclinic-challenge_web_1 (410ef8ae22a35ccbf7b6a2cb8862a00559831d5ae698756770005c39dc37f1bb): Bind for 0.0.0.0:8000 failed: port is already allocated
```
Solução: Troque a port utilizada no arquivo docker-compose.yml para uma que não esteja sendo utilizada.

## API Prescription

### URL: /prescriptions

### Descrição: Cadastro de prescrições

### Método: POST

### Body: 
```json
{
  "clinic": {
    "id": 1
  },
  "physician": {
    "id": 1
  },
  "patient": {
    "id": 1
  },
  "text": "Dipirona 1x ao dia"
} 
```

### Response
```json
{
  "data": {
    "id": 1,
    "clinic": {
      "id": 1
    },
    "physician": {
      "id": 1
    },
    "patient": {
      "id": 1
    },
    "text": "Dipirona 1x ao dia"
  }
} 
```

### Response error
```json
{
  "error": {
    "message": "patient not found",
    "code": "03"
  }
}
```

### Tipos de erro
| code | message                          |
|------|----------------------------------|
| 01   | malformed request                |
| 02   | physician not found              |
| 03   | patient not found                |
| 04   | metrics service not available    |
| 05   | physicians service not available |
| 06   | patients service not available   |
| 07   | connection error                 |

## Testes Unitários

### Comando para executar os testes: 
```bash
docker-compose exec web py.test
```


### Cobertura dos testes

![image](https://user-images.githubusercontent.com/22778168/115154471-64457200-a051-11eb-8e8d-2b0c55be3279.png)


## Pendências e melhorias
- CI
- Estilo do arquivo serializer
- testes unitários dos recursos de retry e timeout dos requests
- Settings do projeto

## Referências

Referências utilizadas para realizar o desafio

| link                                                                               | descrição                                 |
|------------------------------------------------------------------------------------|-------------------------------------------|
| https://www.alura.com.br/curso-online-api-django-3-rest-framework                  | criação da api, serializers               |
| https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/   | retry e timeput dos requests              |
| https://pypi.org/project/requests-cache/                                           | cache das requisições                     |
| https://requests-mock.readthedocs.io                                               | mock de requests e criação de fixtures    |
| https://docs.djangoproject.com/en/3.2/topics/db/transactions/                      | transaction para possibilidar o rollback  |
| https://docs.djangoproject.com/pt-br/3.2/topics/logging/                           | logs                                      |
| https://www.youtube.com/watch?v=xxjzwdtWozI                                        | configuração do postgree e docker         |


