import mysql.connector
from Aplicacao.Treinamento import Treinamento 

class TreinamentoRepository:
    
    def __init__(self, host='localhost', user='root', password='root', database='Treinamentos'):
        self.conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def _abrir_cursor(self):
        """
        Cria e retorna um cursor no formato de dicionário.
        """
        return self.conexao.cursor(dictionary=True)

    def salvar_treinamento(self, treinamento: Treinamento) -> dict:
        """
        Insere um treinamento no banco de dados
        :param treinamento: Objeto contendo um treinamento.
        :return Dicionário com status True/False e mensagem em caso de erro.
        """
        sql = """
            INSERT INTO treinamentos (nome, duracao, instrutor, data_inicio, quantidade_participantes, local)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (
            treinamento.nome,
            treinamento.duracao,
            treinamento.instrutor,
            treinamento.data_inicio,
            treinamento.quantidade_participantes,
            treinamento.local
        )

        try:
            cursor = self._abrir_cursor()
            cursor.execute(sql, valores)
            self.conexao.commit()
            last_id = cursor.lastrowid  
            cursor.close()

            return {"status": True, "id": last_id}

        except Exception as e:
            return {"status": False, "mensagem": str(e)}

    def buscar_todos(self) -> dict:
        """
        Busca todos os treinamentos armazenados no banco de dados
        Dicionário com status True/False e os dados e mensagem em caso de erro.
        """
        sql = "SELECT * FROM treinamentos"
        treinamentos = []

        try:
            cursor = self._abrir_cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()

            for registro in resultados:
                treinamento = Treinamento(registro)
                treinamentos.append(treinamento.to_dict())

            return {"status": True, "dados": treinamentos}

        except Exception as e:
            return {"status": False, "mensagem": str(e)}

    def buscar_por_id(self, id: int) -> dict:
        """
        Busca um treinamento por id
        param: id -> inteiro que representa o id
        Dicionário com as informações do id.
        """
        sql = "SELECT * FROM treinamentos WHERE id = %s"

        try:
            cursor = self._abrir_cursor()
            cursor.execute(sql, (id,))
            resultado = cursor.fetchone()
            cursor.close()

            if not resultado:
                return {"status": False, "mensagem": "Treinamento não encontrado"}

            treinamento = Treinamento(resultado)
            return {"status": True, "dados": treinamento.to_dict()}

        except Exception as e:
            return {"status": False, "mensagem": str(e)}

    def fechar(self):
        """
        Encerra a conexão com o banco de dados.
        """
        self.conexao.close()
