# Trabalho M3
Professor: MS. Geroge de Borba Nardes

## Parte 1
Pesquisar e responder as perguntas sobre os seguintes serviços da AWS:

- Lambda: O que é? Como funciona? Como utilizar?
- DynamoDB: O que é? Como funciona? Como utilizar?
- API Gateway: O que é? Como funciona? Como utilizar?
- IAM: O que é? Como funciona? Como utilizar?

## Parte 2
Criar um CRUD de tarefas usando os serviços pesquisados.

Atributos de uma tarefa:
- Título;
- Descrição;
- Data

A API deve possibilitar:
- Operações Create, Read, Update e Delete (CRUD)
- Busca por tarefas de uma data (exemplo: get_task_by_date(date))

## Recomendações

### 1. Conta e Free Tier 
- **a.** Crie sua conta AWS com cartão (é exigido, mas não será cobrado se usar só o Free Tier).
- **b.** Ative alertas de orçamento no Billing (AWS Budgets) para e-mail quando exceder 1 USD.
- **c.** Após a entrega do trabalho, desabilite todos os serviços que você habilitou.

### 2. API Gateway simples
- **a.** Crie uma HTTP API → adicione rotas POST /tasks, GET /tasks/{id}, PUT /tasks/{id}, DELETE /tasks/{id}.
- **b.** Não é necessário habilitar autenticação neste trabalho.

### 3. Teste rápido
- **a.** Use Postman ou outra ferramenta equivalente para chamar as rotas e testar. Veja os logs no
CloudWatch se preferir.

## Entrega
 - A entrega deve ser em PDF, o qual deve conter as respostas para as perguntas e os links para o repositório do código e para um vídeo de apresentação no trabalho. No vídeo deve ser apresentado o ocódigo e o funcionamento do sistema.

