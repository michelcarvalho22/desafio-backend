# DESENVOLVIMENTO TEMBICI BACKEND VIAGENS

## Uso

API simples e minimalista para utilização de lista das viagens de um usuário específico
além de preenchimento de informações como nota e tipo da viagem

Desenvolvimento em DJANGO/ 3.1 e DJANGO REST FRAMEWORK

## Criação de Usuário

A api busca as informações da tabela USER padrão da autenticação do DJANGO

Pode-se criar um usuário com o comando:
```commandline
python manage.py createsuperuser
```


## Instalação

clonar o projeto em uma pasta que desejar

```commandline
git clone https://github.com/mcribeiro27/desafio-backend-1.git
```

## Desenvolvimento

Para iniciar o desenvolvimento, é necessário clonar o projeto do Github em um diretório de sua preferência:

```commandline
cd "diretorio de sua preferencia"
git clone https://github.com/michelcarvalho22/desafio-backend.git
```

após clonar execute o comando:
```commandline
pip install -r requirements.txt
```



## ENDPOINTS

### Login

```url
http://127.0.0.1:8000/conta/
```
após o login será exibido um token este token deve ser utilizado para fazer as requisições dentro do header conforme abaixo

```json
Autorization: JWT {{ key gerada aqui }}
```

### Tipo de Viagens

```url
http://127.0.0.1:8000/classificacao/
```


### Viagens


```url
http://127.0.0.1:8000/viagem/
```

#### TODOS OS ENDPOINTS ESTÃO PRONTOS PARA UTILIZAÇÃO DOS COMANDOS GET,PUT,DELETE,POST 