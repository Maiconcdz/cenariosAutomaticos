# 🧪 CENÁRIOS DE TESTE - PRESENCE-3060

**Título:** [APP] - Swine - Criação da Funcionalidade de Chamado Sanitário
**Data de geração:** 17/12/2025 17:13

---

## 🎯 CENÁRIOS POSITIVOS
### CT-01: Criação de Chamado Sanitário com Sucesso
**Dado que** o usuário está autenticado e na tela de criação de chamado sanitário  
**Quando** o usuário preencher todos os campos obrigatórios e clicar em "Salvar"  
**Então** o sistema deve criar o chamado sanitário e exibir uma mensagem de confirmação "Chamado criado com sucesso"

### CT-02: Visualização de Chamados Sanitários
**Dado que** o usuário está autenticado e na tela de listagem de chamados sanitários  
**Quando** o usuário clicar em um chamado sanitário específico  
**Então** o sistema deve exibir os detalhes do chamado selecionado corretamente

## 🚫 CENÁRIOS NEGATIVOS  
### CT-03: Falha ao Criar Chamado Sanitário Sem Campos Obrigatórios
**Dado que** o usuário está na tela de criação de chamado sanitário  
**Quando** o usuário tentar salvar o chamado sem preencher os campos obrigatórios  
**Então** o sistema deve mostrar uma mensagem de erro "Por favor, preencha todos os campos obrigatórios"

### CT-04: Falha ao Criar Chamado Sanitário com Dados Inválidos
**Dado que** o usuário está na tela de criação de chamado sanitário  
**Quando** o usuário preencher os campos com dados inválidos (ex: texto em campo numérico) e clicar em "Salvar"  
**Então** o sistema deve mostrar uma mensagem de erro "Dados inválidos, por favor revise as informações"

## 🔍 CENÁRIOS DE BORDA/REGRESSÃO
### CT-05: Acesso à Funcionalidade de Chamado Sanitário
**Dado que** o sistema está em funcionamento e o usuário possui as permissões necessárias  
**Quando** o usuário acessar a funcionalidade de chamado sanitário  
**Então** o sistema deve carregar a tela de criação de chamado sanitário sem apresentar erros ou falhas de carregamento

---

## 📝 NOTAS PARA O TESTADOR
1. Execute os cenários na ordem sugerida
2. Valide tanto frontend quanto backend quando aplicável
3. Documente qualquer desvio encontrado
4. Atualize status no Jira após execução

*Gerado automaticamente pelo QA Automation Tool*
