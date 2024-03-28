# API de Controle e Reserva de Salas de Aula

Este projeto consiste em uma API em Django projetada para facilitar o controle e reserva de salas de aula em uma instituição educacional. A API oferece endpoints para gerenciar salas de aula, horários de disponibilidade e reservas de salas de aula.

## Requisitos

### Software

- Python 3.10
- Django
- MongoDB
- Git (opcional, para gerenciamento de código)

### Hardware

- Computador com capacidade para executar o software necessário
- Conexão com a internet (para instalação de dependências)

### Conhecimentos

- Conhecimento em Python e Django
- Familiaridade com MongoDB
- Noções básicas de API

## Instruções para Execução

1. Clone o repositório para o seu ambiente local:

   ```
   git clone https://github.com/MatheusPCV/api_class.git
   ```

2. Instale as dependências necessárias:

   ```
   cd api_class
   pip install -r requirements.txt
   ```

3. Configure o MongoDB conforme necessário no arquivo `settings.py`.

4. Inicie o servidor de desenvolvimento:
   ```
   python manage.py runserver
   ```

A API estará disponível em `http://localhost:8000/`.

## Endpoints

### 1. Listar todas as Salas de Aula

- **Endpoint:** `/api/salas/`
- **Método:** GET
- **Descrição:** Retorna uma lista de todas as salas de aula disponíveis.

#### Exemplo de Saída:

```json
[
  {
    "id": 1,
    "nome": "Sala A",
    "capacidade": 30,
    "descricao": "Sala de aula para turmas do ensino fundamental."
  },
  {
    "id": 2,
    "nome": "Sala B",
    "capacidade": 25,
    "descricao": "Sala de aula para turmas do ensino médio."
  }
]
```

### 2. Detalhes de uma Sala de Aula

- **Endpoint:** `/api/salas/<id>/`
- **Método:** GET
- **Descrição:** Retorna os detalhes de uma sala de aula específica com base no ID fornecido.

#### Exemplo de Saída:

```json
{
  "id": 1,
  "nome": "Sala A",
  "capacidade": 30,
  "descricao": "Sala de aula para turmas do ensino fundamental."
}
```

### 3. Criar uma Sala de Aula

- **Endpoint:** `/api/salas/criar/`
- **Método:** POST
- **Descrição:** Cria uma nova sala de aula com os detalhes fornecidos.

#### Exemplo de Input:

```json
{
  "nome": "Sala C",
  "capacidade": 20,
  "descricao": "Sala de aula para turmas do ensino médio."
}
```

### 4. Atualizar uma Sala de Aula

- **Endpoint:** `/api/salas/<id>/atualizar/`
- **Método:** PUT
- **Descrição:** Atualiza os detalhes de uma sala de aula existente com base no ID fornecido.

#### Exemplo de Input:

```json
{
  "nome": "Sala A Atualizada",
  "capacidade": 35,
  "descricao": "Sala de aula para turmas do ensino fundamental."
}
```

### 5. Excluir uma Sala de Aula

- **Endpoint:** `/api/salas/<id>/excluir/`
- **Método:** DELETE
- **Descrição:** Remove uma sala de aula existente com base no ID fornecido.

### 6. Listar Horários Disponíveis de uma Sala de Aula

- **Endpoint:** `/api/salas/<id>/horarios/`
- **Método:** GET
- **Descrição:** Retorna uma lista de horários disponíveis para uma sala de aula específica com base no ID fornecido.

### 7. Reservar uma Sala de Aula

- **Endpoint:** `/api/salas/<id>/reservar/`
- **Método:** POST
- **Descrição:** Reserva uma sala de aula específica com base no ID fornecido para um determinado horário.

#### Exemplo de Input:

```json
{
  "horario": "2024-04-01T10:00:00",
  "responsavel": "João da Silva"
}
```

### 8. Cancelar uma Reserva de Sala de Aula

- **Endpoint:** `/api/reservas/<id>/cancelar/`
- **Método:** DELETE
- **Descrição:** Cancela uma reserva de sala de aula existente com base no ID fornecido.
