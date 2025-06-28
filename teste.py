from app.Treinamento import Treinamento
from app.TreinamentoRepository import TreinamentoRepository

TR = TreinamentoRepository()

print(TR.buscar_por_id(1))