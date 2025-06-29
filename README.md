# CRUD de Tarefas com AWS (Lambda, DynamoDB, API Gateway, IAM)

- [Vídeo de apresentação e funcionamento](https://youtu.be/XPwCVHYno70)
- **Alunos:** Arthur de Oliveira Pereira, Gabriel Victor Garcia Teixeira, Gustavo Pedrini, Igor do Carmo, Maria Eduarda Pierri e Ludmila Lais Souza Alves

## Pré-requisitos

- Conta na AWS com Free Tier ativa
- Ativar alertas no AWS Budgets (opcional, mas recomendado)
- Acesso ao console AWS (interface web)
- Aplicação para interagir com endpoints (Insomnia, Postman, etc)

## Estrutura
- Para cada operação do CRUD, foi implementada uma **função Lambda** com integração via **API Gateway** onde os dados são armazenados em uma tabela `tasks` no **DynamoDB**.

---

## Configuração

### 1. Criar a Tabela no DynamoDB

- Abrir o **DynamoDB**
- Clicar em **Create table**
- Table name: `Tasks`
- Partition key: `id` (tipo: String)
- Clicar em **Create table**

---

### 2. Criar as Funções Lambda

| Função Lambda    | Método | Rota API             |
|------------------|--------|----------------------|
| `create_task`    | POST   | `/tasks`             |
| `get_task`       | GET    | `/tasks/{id}`        |
| `update_task`    | PUT    | `/tasks/{id}`        |
| `delete_task`    | DELETE | `/tasks/{id}`        |
| `get_task_by_date` | GET | `/tasks/date?date=...`|

**Para cada função Lambda:**
- No painél **Lambda** clicar em **Create function**
- `Author from scratch`
- Runtime: `Python 3.13`
- Rolar até "Permissions" e:
  - Se for a **primeira função**, selecionar "Create new role with basic Lambda permissions"
  - Para as outras, selecionar "Use an existing role" e reutilizar a mesma

**Depois de criada:**
- Colar cada código presente neste projeto de acordo com a operação
- Clicar em **Deploy**
- Recomendado: Após configurar as permissões no **IAM** (próxima etapa), utilizar os testes do diretório `tests` para cada função

### 3. IAM

**Permissões para interagir com o DynamoDB:**
- Na interface da função Lambda, clicar em **Configuration** e em "Execution role" clicar no role name (link em azul que irá direcionar à aba do **IAM**)
- Clicar em **Add permissions → Attach policies** e adicionar `AmazonDynamoDBFullAccess`

---


### 4 Endpoints API Gateway

- Na aba **API Gateway** clicar em **Create API**
- Escolher **HTTP API** e clicar em **Build**
- Em **Add Integration**, selecionar **Lambda** e escolher `create_task`
- Clique em **Next**

**Adicionar as rotas:**
- `POST /tasks` → `create_task`
- `GET /tasks/{id}` → `get_task`
- `PUT /tasks/{id}` → `update_task`
- `DELETE /tasks/{id}` → `delete_task`
- `GET /tasks/date` → `get_task_by_date`

## Testar

- Em **API Gateway → APIs → <api-criada>** existirá um campo `Default endpoint`
- Utilizando o **Insomnia**, importe o arquivo `insomnia.yaml` presente neste projeto e utilize o `Default endpoint` como **baseURL** no Insomnia
- Para cara endpoint, alterar o ID na URL
