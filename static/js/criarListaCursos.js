export function criarListaCursos(cursos, listaCursos) {
    console.log(cursos);
    cursos.forEach(curso => {
        const details = document.createElement('details');
        details.classList.add('mb-3', 'p-3', 'border', 'rounded', 'bg-white', 'shadow-sm');

        const summary = document.createElement('summary');
        summary.innerText = `${curso.id} - ${curso.nome}`;
        summary.classList.add('fw-bold');

        const conteudo = `
            <p><strong>Duração:</strong> ${curso.duracao} horas</p>
            <p><strong>Instrutor:</strong> ${curso.instrutor}</p>
            <p><strong>Data de Início:</strong> ${curso.data_inicio}</p>
            <p><strong>Participantes:</strong> ${curso.quantidade_participantes}</p>
            <p><strong>Local:</strong> ${curso.local}</p>
        `;

        const div = document.createElement('div');
        div.innerHTML = conteudo;

        details.appendChild(summary);
        details.appendChild(div);
        listaCursos.appendChild(details);
    });
}