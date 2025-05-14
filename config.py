import os

# Configurações do GitHub
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')  # Vai buscar do ambiente, se não encontrar usa string vazia

# Lista de repositórios para busca aleatória
REPOS = [
    {"owner": "facebook", "repo": "react"},
    {"owner": "tensorflow", "repo": "tensorflow"},
    {"owner": "microsoft", "repo": "vscode"},
    {"owner": "django", "repo": "django"},
    {"owner": "python", "repo": "cpython"}
] 
