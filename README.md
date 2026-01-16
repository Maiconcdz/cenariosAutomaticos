🤖 QA Automation – Gerador de Cenários de Teste com IA

Esta automação busca issues da sprint ativa no Jira e utiliza IA para gerar cenários de teste automaticamente, a partir do título (summary) e descrição (description) das tasks.

Os cenários são gerados em Markdown e salvos localmente por issue.

🎯 Objetivo

Acelerar a criação de cenários de teste

Padronizar testes funcionais

Apoiar QA em tarefas, histórias, melhorias e bugs

Reduzir retrabalho quando a task vem pouco detalhada

📋 Pré-requisitos
1️⃣ Ambiente

Python 3.9+

Acesso ao Jira da Agriness

Chave de API da OpenAI

2️⃣ Variáveis de ambiente

Configure as seguintes variáveis antes de rodar o script:

export JIRA_EMAIL="seu.email@agriness.com"
export JIRA_API_TOKEN="SEU_TOKEN_DO_JIRA"
export OPENAI_API_KEY="SUA_CHAVE_OPENAI"


No Windows (PowerShell):

setx JIRA_EMAIL "seu.email@agriness.com"
setx JIRA_API_TOKEN "SEU_TOKEN_DO_JIRA"
setx OPENAI_API_KEY "SUA_CHAVE_OPENAI"

📦 Dependências

Instale as dependências necessárias:

pip install requests openai


💡 Se preferir, crie um requirements.txt:

requests
openai

📁 Estrutura do Projeto
/
├── jira_client.py          # Cliente de integração com Jira
├── ai_generator.py         # Gerador de cenários via IA
├── main.py                 # Script principal
├── cenarios_sprint/        # Cenários gerados (output)
└── logs/
    └── execucao.log        # Log da execução

▶️ Como Executar

Na raiz do projeto, execute:

python main.py

🔍 O que o script faz

Identifica a sprint ativa do board (ID 302)

Busca as issues da sprint

Filtra issues:

Tipos aceitos:

Task, Tarefa

Story

Bug

Improvement, Melhoria

Status aceitos:

To Do

In Progress

Em Andamento

Pronto para Teste

Ready for Test

Envia summary + description para a IA

Gera cenários de teste

Salva um arquivo por issue em:

cenarios_sprint/ISSUE-123_cenarios.md

🧪 Exemplo de Output
cenarios_sprint/
├── PRES-321_cenarios.md
├── PRES-328_cenarios.md
└── PRES-335_cenarios.md


Cada arquivo contém:

Cenários positivos

Cenários negativos

Casos de exceção

Fluxos alternativos

Validações funcionais

⚙️ Configurações Importantes

No arquivo main.py:

MAX_ISSUES = 5


Altere esse valor para definir quantas issues da sprint serão processadas por execução.

🛑 Possíveis Erros e Soluções
❌ Nenhuma issue encontrada

Verifique se existe sprint ativa

Confirme se as issues estão nos status permitidos

Confirme se as issues possuem descrição ou critérios mínimos

❌ Erro de autenticação Jira

Verifique JIRA_EMAIL

Gere um novo API Token no Jira

Confirme permissões no board

❌ Erro OpenAI

Verifique a variável OPENAI_API_KEY

Confirme se a chave está ativa

Verifique limite de uso da API

📌 Observações

O script não altera nada no Jira

Apenas lê dados e gera arquivos locais

Pode ser executado localmente ou em pipeline (CI/CD)

Ideal rodar no início da sprint ou antes do planejamento de testes

🚀 Próximos Passos (Evoluções Possíveis)

Publicar cenários automaticamente no Jira

Integração com Xray / Zephyr

Gerar casos de teste automatizados

Trigger automático ao mover issue para Ready for Test
