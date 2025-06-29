import { get } from './get.js';
import { criarListaCursos } from './criarListaCursos.js'

const listaCursos = document.getElementById('listaCursos');

window.addEventListener('DOMContentLoaded', async () => {
    const url = "/api/treinamentos";
    const cursos = await get(url);
    criarListaCursos(cursos, listaCursos);
});
