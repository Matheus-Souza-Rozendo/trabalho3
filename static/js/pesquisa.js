import { get} from './get.js';
import { criarListaCursos } from './criarListaCursos.js'


const listaCursos = document.getElementById('listaCursos');
const btnPesquisar = document.getElementById('btnPesquisar');
const campoId = document.getElementById('pesquisaId');


async function pesquisarPorId() {
    const id = parseInt(campoId.value);

    if (isNaN(id) || id <= 0) {
        alert("Informe um ID válido.");
        return;
    }
    const url = "/api/treinamentos/"+String(id);
    const curso = await get(url);

    listaCursos.innerHTML = '';

    if (curso) {
        criarListaCursos([curso], listaCursos);
    } else {
        listaCursos.innerHTML = `<div class="alert alert-warning">Treinamento com ID ${id} não encontrado.</div>`;
    }
}


btnPesquisar.addEventListener('click', pesquisarPorId);
