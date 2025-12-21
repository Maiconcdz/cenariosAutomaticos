# config.py
# Configurações do projeto

GEMINI_API_KEY = "AIzaSyBlmN_H5m6YmWtWDVJi4ioVzfQUeWJAgnI"  # 🔥 SUA CHAVE AQUI 🔥

JIRA_CONFIG = {
    "base_url": "https://agriness-team.atlassian.net",
    "board_id": 302,
    "email": "JIRA_EMAIL",
    "token": "JIRA_API_TOKEN"  # Token do Lucas (revogar depois!)
}

# Tipos de issue que devem gerar cenários
ISSUE_TYPES = ["Tarefa", "Improvement", "Melhoria", "Task", "Story"]

# Status que indicam "pronto para teste"
READY_STATUSES = ["Em Andamento", "Pronto para Teste", "Ready for Test", "In Progress"]