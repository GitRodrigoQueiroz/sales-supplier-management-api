
# API REST para Gestão de Suppliers, Transações e Analytics

## Introdução:
Este projeto é uma API REST desenvolvida com FastAPI para gerenciar suppliers, transações e gerar dados analíticos. Ele inclui autenticação baseada em JWT, consultas eficientes, e segue boas práticas de segurança.

##  Tecnologias Utilizadas:
- 🔄  **Gerenciador de dependências**: [uv](https://github.com/astral-sh/uv) 
- 🐍 **Linguagem**: Python 3.10
- ⚡ **API Framework**: FastAPI
- 🗄️ **Banco de Dados**: PostgreSQL (SQLAlchemy e Alembic para ORM e migrações)
- 🔐 **Autenticação**: JWT (OAuth2)
- 📦 **Containerização**: Docker & Docker Compose
- 🧪 **Testes**: Pytest
- 🛠️ **Automação de Tarefas**: Makefile


## 🛠️ Instalação e Execução:

### Clonando o Repositório:
```sh
$ git clone https://github.com/GitRodrigoQueiroz/sales-supplier-management-api.git
$ cd sales-supplier-management-api

```

### Criação do ambiente e instalação das dependências:

```bash
uv sync
source .venv/bin/activate  
```

### Configuração do ambiente:
Crie um arquivo **.env** na raiz do repositório com as seguintes variáveis:
```ini
USER=${USER}
PASSWORD=${PASSWORD}
HOST=${HOST}
PORT=${PORT}
DATABASE=${DATABASE}
SECRET_KEY=${SECRET_KEY}
ALGORITHM=${ALGORITHM}
ACCESS_TOKEN_EXPIRE_MINUTES=${ACCESS_TOKEN_EXPIRE_MINUTES}
```

Neste projeto, incluímos um arquivo **.env** de exemplo para demonstrar a configuração das variáveis de ambiente e facilitar a replicação do ambiente de desenvolvimento. 

### Configuração do Banco de Dados:

Neste projeto, utilizaremos um banco postgres local gerenciado via `Docker`. No terminal, execute os seguintes comandos:


```bash
$ make launch-db
$ make create-db 
$ make seed-db
```

1. `launch-db` é utilizado para inicializar o banco de dados como um container docker.
2. `create-db` é utilizado para construir as tabelas e relações definidas nos ORM's.
3. `seed-db` é utilizado para popular o banco de dados com dados de exemplo, facilitando os testes.

### Executando a API:
```sh
$ make lauch-api
```

Acesse `http://localhost:8000/docs` para visualizar a **Documentação Swagger:** gerada automaticamente pelo FastAPI.


##  🔐  Segurança

Esta API implementa um sistema de segurança utilizando **JWT (JSON Web Token)** para garantir a autenticação de usuários em rotas protegidas. Abaixo está uma visão geral da estratégia utilizada.

### 1. Estrutura de Usuários

A aplicação utiliza uma tabela **user**, onde o primeiro usuário é um **admin**. 

A tabela **user** contém campos para usuário, CPF e senha. A senha e o CPF do usuário é **hasheada** utilizando o algoritmo `sha256_crypt` do pacote `passlib` para garantir a segurança dos dados sensíveis. Nesta aplicação, considera-se que todos os usuários cadastrados (inclusive o admin) têm total acesso à todos os dados cadastrados.


### 2. OAuth2 com JWT

A API utiliza a especificação **OAuth2** com o fluxo de senha, um padrão seguro para autenticação. Isso é implementado no **FastAPI** através do `OAuth2PasswordBearer`.

### 3. Login e JWT - JSON Web Token

Para realizar o login, o usuário envia seu **nome de usuário** e **senha**. Caso sejam válidos, um **token JWT** é gerado e retornado para o usuário. Este token será utilizado para autenticar o usuário em todas as rotas protegidas da API. O token é transmitido nas requisições subsequentes no cabeçalho **Authorization**. 

O **JWT** contém informações (payload) sobre o usuário, como o nome de usuário (`sub`), e é assinado com uma **chave secreta** (armazenada na variável `SECRET_KEY`) e um **algoritmo seguro** (definido na variável `ALGORITHM`).


## Endpoints Principais

### Autenticação:
- `POST /auth/register` - Registro de novo usuário
- `POST /auth/login` - Login e geração de JWT

### Suppliers:
- `POST /suppliers/` - Criar supplier
- `GET /suppliers/` - Listar suppliers com filtros
- `GET /suppliers/{id}` - Buscar supplier por ID
- `PUT /suppliers/{id}` - Atualizar supplier
- `DELETE /suppliers/{id}` - Remover supplier

### Transações:
- `POST /transactions/` - Criar transação
- `GET /transactions/` - Listar transações com filtros

### Analytics:
- `GET /analytics/sales` - Total de vendas por supplier/parte
- `GET /analytics/warranties` - Número de garantias emitidas



## Testes Automatizados
Para rodar os testes:
```sh
$ pytest tests/
```

---


## Autor
1. Desenvolvido por [Rodrigo Silvestre Queiroz](https://github.com/GitRodrigoQueiroz).
2. Consultar o arquivo `DESIGN.md` para mais informações sobre o design do projeto.