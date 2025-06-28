### 2.1. Envio de Dados de Treinamentos (POST)
**Descrição**: O serviço deve permitir que dados de treinamentos sejam enviados para o servidor, incluindo informações detalhadas como o nome do treinamento, duração, nome do instrutor, data de início, quantidade de participantes, e local do treinamento.

- **Método HTTP**: POST
- **Formato de Dados**: JSON
- **Endereço**: `/api/treinamentos`

**Parâmetros**:
- Código identificador (gerado automaticamente no servidor)
- Nome do treinamento
- Duração (em horas)
- Nome do instrutor
- Data de início (formato YYYY-MM-DD)
- Quantidade de participantes
- Local do treinamento

**Exemplo de Requisição**:
```json
{
    "nome_treinamento": "Treinamento de Excel Avançado",
    "duracao": 8,
    "instrutor": "João Silva",
    "data_inicio": "2025-07-01",
    "quantidade_participantes": 25,
    "local": "Sala 203"
}
```

**Resposta Esperada**:
- **Código de Status**: 201 (Created)
- **Corpo da Resposta**:
```json
{
    "status": "sucesso",
    "mensagem": "Treinamento registrado com sucesso",
    "id_treinamento": 101
}
```

### 2.2. Obter Dados de Todos os Treinamentos (GET)
**Descrição**: O serviço deve permitir que todos os dados de treinamentos armazenados sejam recuperados do servidor.

- **Método HTTP**: GET
- **Endereço**: `/api/treinamentos`

**Resposta Esperada**:
- **Código de Status**: 200 (OK)
- **Corpo da Resposta**:
```json
[
    {
        "id": 101,
        "nome_treinamento": "Treinamento de Excel Avançado",
        "duracao": 8,
        "instrutor": "João Silva",
        "data_inicio": "2025-07-01",
        "quantidade_participantes": 25,
        "local": "Sala 203"
    },
    {
        "id": 102,
        "nome_treinamento": "Gestão de Projetos",
        "duracao": 12,
        "instrutor": "Maria Oliveira",
        "data_inicio": "2025-07-15",
        "quantidade_participantes": 20,
        "local": "Sala 205"
    }
]
```

### 2.3. Obter Histórico de Treinamento Específico (GET)
**Descrição**: O serviço deve permitir que, fornecendo o código identificador de um treinamento, sejam obtidos os dados específicos desse treinamento.

- **Método HTTP**: GET
- **Endereço**: `/api/treinamentos/{id}`

**Parâmetros**:
- `id`: Código identificador do treinamento

**Resposta Esperada**:
- **Código de Status**: 200 (OK)
- **Corpo da Resposta**:
```json
{
    "id": 101,
    "nome_treinamento": "Treinamento de Excel Avançado",
    "duracao": 8,
    "instrutor": "João Silva",
    "data_inicio": "2025-07-01",
    "quantidade_participantes": 25,
    "local": "Sala 203"
}
```