# 🧱 Principais Classes do Sistema

## 1. Treinamento
**Responsabilidade**: Representar os dados e comportamentos relacionados a um treinamento específico.

### Atributos:
- **id**: Identificador único (gerado automaticamente).
- **nome**: Nome do treinamento.
- **duracao**: Duração em horas.
- **instrutor**: Nome do instrutor.
- **data_inicio**: Data de início.
- **quantidade_participantes**: Número de participantes.
- **local**: Local do treinamento.

### Métodos:
- **privado**: `validar_dados()`: Verificar a consistência dos dados na hora da criação da classe.

---

## 2. TreinamentoRepository
**Responsabilidade**: Gerenciar a persistência dos objetos Treinamento no banco de dados.

### Atributos:
- **conexao**: armazena a conexão com o banco de dados

### Métodos:
- `salvar(treinamento: Treinamento)`: Salvar um novo treinamento.
- `buscar_por_id(id: int)`: Recuperar um treinamento pelo ID.
- `listar_todos()`: Listar todos os treinamentos.
- `fechar_conexao()`: Encerrar a conexão com o banco de dados.

---


# 🧭 Justificativa e Boas Práticas

### SOLID
As classes seguem os princípios SOLID para garantir um design robusto e de fácil manutenção.

### Responsabilidade Única
Cada classe tem uma única responsabilidade, facilitando a compreensão e a manutenção do código.

### Encapsulamento
Os detalhes de implementação são ocultados, expondo apenas o necessário para a interação com outras partes do sistema.

### Baixo Acoplamento
As classes interagem entre si de forma minimizada, permitindo alterações em uma classe sem impactar significativamente as outras.

### Alta Coesão
As classes são coesas, ou seja, seus métodos e atributos estão intimamente relacionados à sua responsabilidade principal.