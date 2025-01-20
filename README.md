# API Em Python/Django

## Primeiro, instale as dependências com o seguinte comando:

```bash
pip install django-environ
```
## Insira as credencias de Conexão com o banco de dados Postgres no arquivo .env

DB_NAME=Nome_do_Banco</br>
DB_USER=Usuario</br>
DB_PASSWORD=Senha</br>
DB_HOST=Host</br>
DB_PORT=Porta</br>

obs: Crie o arquivo na raiz do projeto, caso não seja criado.

## Criar Super usuário
Para acessar o painel administrativo do Django, crie um super usuário:</br>

```bash
python manage.py createsuperuser
```

Forneça um nome de usuário, e-mail e senha para o super usuário.</br>

## Acessar a tela inicial e o Painel Administrativo:

Tela inicial: http://127.0.0.1:8000/ </br>
painel administrativo do Django: http://127.0.0.1:8000/admin</br>

Use o super usuário que você criou anteriormente para fazer login.</br>

## Documentação da API

### Autenticação
**Todos os endpoints exigem autenticação via JWT. Para isso, siga os passos:**

#### 1. Obter o token de acesso:

 Método | Endpoint | Descrição |
|--------|----------|------------|
| POST   | `/api/token/` |Obter o token de acesso |


#### Payload:
```json
{
"username": "victor",
"password": "Victo2025!"
}
```
#### Resposta:
```json
{
"access": "jwt_token_de_acesso",
"refresh": "jwt_token_de_refresh"
}

```
#### 2. Enviar o token no header das requisições:

Authorization: Bearer jwt_token_de_acesso

### 1. Tecnologias
**URL base:** `/api/tecnologias/`

#### Endpoints
| Método | Endpoint | Descrição |
|--------|----------|------------|
| GET    | `/api/tecnologias/` | Listar todas as tecnologias |
| POST   | `/api/tecnologias/` | Criar uma nova tecnologia |
| GET    | `/api/tecnologias/{id}/` | Obter detalhes de uma tecnologia |
| PUT    | `/api/tecnologias/{id}/` | Atualizar uma tecnologia existente |
| DELETE | `/api/tecnologias/{id}/` | Remover uma tecnologia |

#### Exemplo de payload (POST):
```json
{
  "nome": "Python"
}
```
### 2. Programadores
**URL base:** ``/api/programadores/``

### Endpoints

 Método | Endpoint | Descrição |
|--------|----------|------------|
| GET    | `/api/programadores/` | Listar todos os programadores |
| POST   | `/api/programadores/` |Criar um novo programador |
| GET    | `/api/programadores/{id}/` | Obter detalhes de um programador |
| PUT    | `/api/programadores/{id}/` | Atualizar um programador existente |
| DELETE | `/api/programadores/{id}/` | Remover um programador |

#### Exemplo de payload (POST):
```json
{
  "nome": "Alice",
  "tecnologias": [1, 2] // IDs das tecnologias que o programador domina
}
```
### 3. Projetos
**URL base:** ``/api/projetos/``
### Endpoints

 Método | Endpoint | Descrição |
|--------|----------|------------|
| GET    | `/api/projetos/` | Listar todos os projetos |
| POST   | `/api/projetos/` |Criar um novo projeto |
| GET    | `/api/projetos/{id}/` | Obter detalhes de um projeto |
| PUT    | `/api/projetos/{id}/` | Atualizar um projeto existente |
| DELETE | `/api/projetos/{id}/` | Remover um projetos |

#### Exemplo de payload (POST):
```json
{
    "nome": "Projeto X",
    "data_inicial": "2025-01-01",
    "data_final": "2025-06-01",
    "tecnologias": [1, 2] // IDs das tecnologias exigidas pelo projeto
}
```
#### 4. Alocações
**URL base:** ``/api/alocacoes/``

### Endpoints

 Método | Endpoint | Descrição |
|--------|----------|------------|
| GET    | `/api/alocacoes/` | Listar todos os projetos |
| POST   | `/api/alocacoes/` |Criar um novo projeto |
| DELETE | `/api/alocacoes/{id}/` | Remover um projetos |

#### Exemplo de payload (POST):
```json
{
    "projeto": 1, 
    "desenvolvedor": 2, 
    "horas": 40
}
```
## 
