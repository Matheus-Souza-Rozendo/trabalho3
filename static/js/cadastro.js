import post from './post.js';


const form = document.getElementById('formularioTreinamento');

form.addEventListener('submit', async function(e) {
  e.preventDefault();

  if (!form.checkValidity()) {
    return;
  }

  // Coletando valores do formulário
  const nomeTreinamento = document.getElementById('nomeTreinamento').value;
  const duracao = parseInt(document.getElementById('duracao').value);
  const instrutor = document.getElementById('instrutor').value;
  const dataInicio = document.getElementById('dataInicio').value;
  const quantidadeParticipantes = parseInt(document.getElementById('quantidadeParticipantes').value);
  const local = document.getElementById('local').value;

  const body = {
    nome: nomeTreinamento,
    duracao: duracao,
    instrutor: instrutor,
    data_inicio: dataInicio,
    quantidade_participantes: quantidadeParticipantes,
    local: local
  };
  console.log(body)
  const url= "/api/treinamentos";
  const resposta = await post(url, body);
  console.log(resposta);
  alert(resposta.mensagem);
});
