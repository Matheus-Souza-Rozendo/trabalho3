from flask import Flask, render_template, request, jsonify
from app.Treinamento import Treinamento
from app.TreinamentoRepository import TreinamentoRepository

# Criação do app Flask
app = Flask(__name__)

# Definição das rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/pesquisa')
def pesquisa():
    return render_template('pesquisa.html')


# Rota POST para receber dados do formulário de cadastro
@app.route('/api/treinamentos', methods=['POST'])
def cadastrar():
    """
    Função para cadastrar um novo treinamento.

    Retorna:
        dict: Status da operação e mensagem.
    """
    # Pegando os dados enviados via POST
    data = request.get_json()
    
    if data:
        treinamento = Treinamento(data)
        valida = treinamento.validar_dados()
        
        if valida['status']:
            TR = TreinamentoRepository()
            resposta = TR.salvar_treinamento(treinamento)
            TR.fechar()  # Garantir que o repositório seja fechado após o uso

            if resposta['status']:
                return jsonify({"status": "sucesso", "mensagem": "Treinamento registrado com sucesso", "id": resposta['id']}), 201
            return jsonify({'status': "erro", "mensagem": resposta['mensagem']}), 400
        return jsonify({'status': 'erro', "mensagem": valida['mensagem']}), 400
    
    return jsonify({'status': 'erro', 'mensagem': 'Faltando dados'}), 400

# Rota POST para receber dados do formulário de cadastro
@app.route('/api/treinamentos', methods=['GET'])
def buscar():
    """
    Função para buscar todos os treinamentos do repositório.
    
    Retorna:
        dict: Dados dos treinamentos ou mensagem de erro.
    """
    TR = TreinamentoRepository()
    
    try:
        resposta = TR.buscar_todos()
        
        if resposta['status']:
            return jsonify(resposta['dados']), 200
        else:
            return jsonify({"status": "erro", "mensagem": resposta['mensagem']}), 500
    finally:
        # Garantir que o repositório seja fechado, mesmo em caso de erro
        TR.fechar()



# Rota POST para receber dados do formulário de cadastro
@app.route('/api/treinamentos/<int:id>', methods=['GET'])
def buscar_por_id(id: int):
    """
    Função para buscar um treinamento pelo ID.

    Args:
        id (int): O ID do treinamento a ser buscado.

    Retorna:
        dict: Dados do treinamento ou mensagem de erro.
    """
    TR = TreinamentoRepository()
    
    try:
        resposta = TR.buscar_por_id(id)
        
        if resposta['status']:
            return jsonify(resposta['dados']), 200
        else:
            return jsonify({"status": "erro", "mensagem": resposta['mensagem']}), 404
    finally:
        TR.fechar()  # Garantir o fechamento do repositório


# Execução do app
if __name__ == '__main__':
    app.run()