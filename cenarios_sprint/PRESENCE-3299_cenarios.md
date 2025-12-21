# 🧪 CENÁRIOS DE TESTE - PRESENCE-3299

**Título:** [PRESENCE-APP] Validação e2e offline QA
**Data de geração:** 17/12/2025 17:13

---

## 🎯 CENÁRIOS POSITIVOS
### CT-01: Persistência de Dados Offline
**Dado que** o usuário está offline e possui dados não sincronizados  
**Quando** o usuário fecha e reabre o aplicativo  
**Então** os dados devem persistir e estar disponíveis na interface do aplicativo

### CT-02: Sincronização Automática ao Reconectar
**Dado que** o usuário está offline e realizou ações que geraram dados  
**Quando** o usuário reconecta à internet  
**Então** os dados devem ser sincronizados automaticamente com o servidor

### CT-03: Envio de Checklist com Imagem
**Dado que** o usuário aplicou um checklist offline e anexou uma imagem  
**Quando** o usuário reconecta à internet  
**Então** o checklist e a imagem devem ser enviados e associados corretamente no servidor

## 🚫 CENÁRIOS NEGATIVOS  
### CT-04: Tentativa de Finalizar Atendimento sem Checklist Completo
**Dado que** o usuário está offline e possui um atendimento com checklist obrigatório  
**Quando** o usuário tenta finalizar o atendimento sem preencher todos os itens do checklist  
**Então** o botão de finalizar deve permanecer desabilitado e uma mensagem de erro deve ser exibida

## 🔍 CENÁRIOS DE BORDA/REGRESSÃO
### CT-05: Sincronização de Múltiplas Ações
**Dado que** o usuário realizou várias ações offline (agendamentos, atendimentos, checklist)  
**Quando** o usuário reconecta à internet e abre o aplicativo  
**Então** todas as ações devem ser sincronizadas na ordem correta e os dados devem ser validados quanto à integridade no servidor

---

## 📝 NOTAS PARA O TESTADOR
1. Execute os cenários na ordem sugerida
2. Valide tanto frontend quanto backend quando aplicável
3. Documente qualquer desvio encontrado
4. Atualize status no Jira após execução

*Gerado automaticamente pelo QA Automation Tool*
