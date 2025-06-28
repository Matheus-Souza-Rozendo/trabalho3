/TRABALHO3
│
├── /app
│   ├── __init__.py         # Inicialização do app Flask
│   ├── routes.py           # Rotas da aplicação
│   ├── Treinamento.py      # Classe treinamento
|   ├── TreinamentoRepository.py  # Classe Treinamento Repository
│   
│
├── /static
│   ├── /css
        ├── style.css  # arquivo de estilos
│   ├── /js 
        ├── get.js  # função para fazer requisição get
        ├── post.js # função para fazer requisição post
│
├── /templates
│   └── index.html  # tela inicial
│   └── cadastro.html # tela para cadastrar o curso
|   └── cursos.html # tela para buscar todos os cursos
|   └── pesquisa.html # tela para buscar curso por id
├── run.py                  # Arquivo principal que executa o app