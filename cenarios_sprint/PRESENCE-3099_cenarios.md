# 🧪 CENÁRIOS DE TESTE - PRESENCE-3099

**Título:** [APP] - Análise de consumo de ração - Consumo por carga, por tipo e por grupo de ração
**Data de geração:** 17/12/2025 17:13

---

## 🎯 CENÁRIOS POSITIVOS
### CT-01: Análise de consumo de ração por carga
**Dado que** o usuário está autenticado e acessa a funcionalidade de análise de consumo de ração  
**Quando** o usuário seleciona a holding, a fazenda e o grupo de animais corretos e define um período de análise  
**Então** o sistema deve exibir os dados de consumo por carga de ração, incluindo nome da ração, período, CMD Real, CMD Previsto, Diferença e Consumo Ração/Cab.

### CT-02: Análise de consumo de ração por tipo
**Dado que** o usuário está na tela de análise de consumo de ração  
**Quando** o usuário seleciona a opção de consumo por tipo de ração e define um período de análise  
**Então** o sistema deve apresentar os dados de consumo por tipo de ração, incluindo nome da ração, período, CMD Real, CMD Previsto, Diferença e Consumo Ração/Cab.

### CT-03: Análise de consumo de ração por grupo
**Dado que** o usuário está na funcionalidade de análise de consumo de ração  
**Quando** o usuário escolhe a opção de consumo por grupo de ração e define um período de análise  
**Então** o sistema deve mostrar os dados de consumo por grupo de ração, incluindo nome da ração, período, CMD Real, CMD Previsto, Diferença e Consumo Ração/Cab.

## 🚫 CENÁRIOS NEGATIVOS  
### CT-04: Falha ao tentar acessar análise sem autenticação
**Dado que** o usuário não está autenticado  
**Quando** o usuário tenta acessar a funcionalidade de análise de consumo de ração  
**Então** o sistema deve redirecionar o usuário para a tela de login e exibir uma mensagem de erro informando que a autenticação é necessária.

### CT-05: Período de análise inválido
**Dado que** o usuário está autenticado e acessa a funcionalidade de análise de consumo de ração  
**Quando** o usuário define um período de análise onde a data final é anterior à data inicial  
**Então** o sistema deve exibir uma mensagem de erro informando que o período de análise é inválido.

## 🔍 CENÁRIOS DE BORDA/REGRESSÃO
### CT-06: Validação de dados de consumo com dados válidos
**Dado que** o usuário está autenticado e acessa a funcionalidade de análise de consumo de ração  
**Quando** o usuário seleciona uma holding, uma fazenda e um grupo de animais válidos e define um período de análise válido  
**Então** o sistema deve retornar os dados de consumo corretamente formatados e sem erros, garantindo que a funcionalidade não quebre com dados válidos.

---

## 📝 NOTAS PARA O TESTADOR
1. Execute os cenários na ordem sugerida
2. Valide tanto frontend quanto backend quando aplicável
3. Documente qualquer desvio encontrado
4. Atualize status no Jira após execução

*Gerado automaticamente pelo QA Automation Tool*
