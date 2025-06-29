export default async function post(url, body) {
  try {
    // Fazendo a requisição POST
    const resposta = await fetch(url, {
      method: 'POST',  // Método POST
      headers: {
        'Content-Type': 'application/json',  // Definindo o tipo de conteúdo como JSON
      },
      body: JSON.stringify(body),  // Convertendo o corpo para JSON
    });
    const dados = await resposta.json()
    // Verificando se a resposta foi bem-sucedida
    if (!resposta.ok) {
      throw new Error(`Erro na requisição: ${resposta.status}`);
    }
  
    
    // Retornando o objeto JSON
    return dados;
  } catch (erro) {
    console.error('Erro ao fazer a requisição:', erro);
    return null;
  }
}
