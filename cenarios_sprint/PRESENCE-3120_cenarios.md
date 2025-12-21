# 🧪 CENÁRIOS DE TESTE - PRESENCE-3120

**Título:** [APP] - Poultry - Criação da Funcionalidade de Chamado Sanitário
**Data de geração:** 17/12/2025 15:29

---

## 🎯 CENÁRIOS POSITIVOS
### CT-01: Criação de Chamado Sanitário com Sucesso
**Dado que** o usuário está autenticado no aplicativo Poultry  
**Quando** o usuário navega até a funcionalidade de Chamado Sanitário e preenche todos os campos obrigatórios corretamente  
**Então** o sistema deve criar o chamado sanitário e exibir uma mensagem de confirmação de sucesso

### CT-02: Visualização de Chamados Sanitários
**Dado que** existem chamados sanitários previamente criados no sistema  
**Quando** o usuário acessa a lista de chamados sanitários  
**Então** o sistema deve exibir todos os chamados sanitários com suas respectivas informações (data, status, descrição)

## 🚫 CENÁRIOS NEGATIVOS  
### CT-03: Criação de Chamado Sanitário com Campos Obrigatórios Vazios
**Dado que** o usuário está autenticado no aplicativo Poultry  
**Quando** o usuário navega até a funcionalidade de Chamado Sanitário e tenta criar um chamado sem preencher os campos obrigatórios  
**Então** o sistema deve mostrar uma mensagem de erro indicando que os campos obrigatórios devem ser preenchidos

### CT-04: Criação de Chamado Sanitário com Dados Inválidos
**Dado que** o usuário está autenticado no aplicativo Poultry  
**Quando** o usuário preenche os campos obrigatórios com dados inválidos (ex: caracteres especiais em campos de texto)  
**Então** o sistema deve mostrar uma mensagem de erro indicando que os dados fornecidos são inválidos

## 🔍 CENÁRIOS DE BORDA/REGRESSÃO
### CT-05: Acesso à Funcionalidade de Chamado Sanitário
**Dado que** o usuário está autenticado e possui permissões adequadas  
**Quando** o usuário acessa a funcionalidade de Chamado Sanitário  
**Então** o sistema deve carregar a interface da funcionalidade sem apresentar erros ou falhas de carregamento

---

## 📝 NOTAS PARA O TESTADOR
1. Execute os cenários na ordem sugerida
2. Valide tanto frontend quanto backend quando aplicável
3. Documente qualquer desvio encontrado
4. Atualize status no Jira após execução

*Gerado automaticamente pelo QA Automation Tool*
