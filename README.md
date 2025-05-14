# 📊 Ferramenta de Monitoramento de Atividades no GitHub
Ferramenta web desenvolvida com Flask para monitorar e visualizar atividades de desenvolvimento em repositórios GitHub. Ideal para acompanhar o progresso de equipes de desenvolvimento, analisando commits e pull requests ao longo do tempo.

🚀 Funcionalidades
Visualização de Commits: Gráficos que mostram a frequência de commits nos últimos 30 dias.
Análise de Pull Requests: Exibição de pull requests criados, abertos e fechados recentemente.
Seleção de Repositórios: Monitoramento de múltiplos repositórios definidos na configuração.
Interface Web Intuitiva: Dashboard interativo para facilitar a análise das atividades.

🛠️ Tecnologias Utilizadas
Python 3.11
Flask
GitHub API
HTML/CSS/JavaScript

📦 Instalação
1. Clone o repositório:

```bash 
git clone https://github.com/AkaLuiz/FerramentaMonitoramento.git
cd FerramentaMonitoramento 
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o token do GitHub:
Crie um arquivo config.py com o seguinte conteúdo:
```bash
GITHUB_TOKEN = 'seu_token_aqui'
REPOS = [
    {'owner': 'usuario', 'repo': 'nome_do_repositorio'},
    # Adicione mais repositórios conforme necessário
]
```

🔐 Nota: Para gerar um token de acesso pessoal, acesse https://github.com/settings/tokens.

5. Execute a aplicação:

```bash
python app.py
```
Acesse http://localhost:5000 no seu navegador para visualizar o dashboard.

📁 Estrutura do Projeto
```arduino
FerramentaMonitoramento/
├── app.py
├── config.py
├── requirements.txt
├── static/
│   └── ... (arquivos estáticos como CSS e JS)
├── templates/
│   ├── index.html
│   └── repository.html
└── ...
```




