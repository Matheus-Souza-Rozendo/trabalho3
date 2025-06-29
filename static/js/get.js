export async function get(url) {
  try {
    // Fazendo a requisição GET
    const resposta = await fetch(url);
    
    // Verificando se a resposta foi bem-sucedida
    if (!resposta.ok) {
      throw new Error(`Erro na requisição: ${resposta.status}`);
    }
    
    // Convertendo a resposta para JSON
    const dados = await resposta.json();
    
    // Retornando o objeto JSON
    return dados;
  } catch (erro) {
    console.error('Erro ao fazer a requisição:', erro);
    return null;
  }
}
