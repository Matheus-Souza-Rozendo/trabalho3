import datetime

class Treinamento:
    """
    Classe que representa um treinamento, com validação de dados e formatação de saída.
    """

    def __init__(self, dados: dict):
        """
        Inicializa um objeto Treinamento a partir de um dicionário de dados.

        :param dados: Dicionário contendo os campos do treinamento.
        """
        self.id = dados.get("id")
        self.nome = dados.get("nome")
        self.duracao = dados.get("duracao")
        self.instrutor = dados.get("instrutor")
        self.quantidade_participantes = dados.get("quantidade_participantes")
        self.local = dados.get("local")

        data_inicio = dados.get("data_inicio")

        # Se for datetime.date, converte para string no formato YYYY-MM-DD
        if isinstance(data_inicio, datetime.date):
            self.data_inicio = data_inicio.strftime("%Y-%m-%d")
        else:
            self.data_inicio = data_inicio

    def validar_dados(self) -> dict:
        """
        Valida os campos do treinamento.

        :return: Dicionário com status True/False e mensagem em caso de erro.
        """
        campos_texto = [self.nome, self.instrutor, self.data_inicio, self.local]

        for campo in campos_texto:
            if campo is None or campo == "":
                return {"status": False, "mensagem": "Todos os campos de texto devem ser preenchidos"}

        if self.duracao is None or self.duracao < 1:
            return {"status": False, "mensagem": "A duração deve ser maior que zero"}

        if self.quantidade_participantes is None or self.quantidade_participantes < 1:
            return {"status": False, "mensagem": "O curso deve ter pelo menos 1 participante"}

        if self.id is not None and self.id < 0:
            return {"status": False, "mensagem": "ID inválido"}

        # Validação do formato da data com datetime.strptime
        try:
            datetime.datetime.strptime(self.data_inicio, "%Y-%m-%d")
        except (ValueError, TypeError):
            return {"status": False, "mensagem": "Data no formato inválido (use YYYY-MM-DD)"}

        return {"status": True}

    def __get_data_formatada(self) -> str:
        """
        Retorna a data de início no formato DD-MM-YYYY, ou uma string vazia se a data não for válida.
        """
        try:
            data = datetime.datetime.strptime(self.data_inicio, "%Y-%m-%d")
            return data.strftime("%d-%m-%Y")
        except (ValueError, TypeError):
            return ""


    def to_dict(self) -> dict:
        """
        Retorna um dicionário com os dados do treinamento, com a data formatada.

        :return: Dicionário dos dados do treinamento.
        """
        return {
            "id": self.id,
            "nome": self.nome,
            "duracao": self.duracao,
            "instrutor": self.instrutor,
            "data_inicio": self.__get_data_formatada(),
            "quantidade_participantes": self.quantidade_participantes,
            "local": self.local
        }
