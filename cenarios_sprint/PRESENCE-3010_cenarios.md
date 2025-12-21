# 🧪 CENÁRIOS DE TESTE - PRESENCE-3010

**Título:** [ANÁLISE] - Homologação dos dados migrados (presence - bff)
**Data de geração:** 17/12/2025 17:12

---

## 🎯 CENÁRIOS POSITIVOS
### CT-01: Validação de dados migrados para a corporação COPÉRDIA
**Dado que** a versão do APP está apontando para HOMOLOGAÇÃO e os dados migrados de Presence e Corp foram gerados no dia 01/08/2025  
**Quando** o usuário acessa os dados da corporação COPÉRDIA  
**Então** o sistema deve exibir corretamente todas as informações migradas para a corporação COPÉRDIA.

### CT-02: Validação de dados migrados para a corporação Alimentos Estrela
**Dado que** a versão do APP está apontando para HOMOLOGAÇÃO e os dados migrados de Presence e Corp foram gerados no dia 01/08/2025  
**Quando** o usuário acessa os dados da corporação Alimentos Estrela  
**Então** o sistema deve exibir corretamente todas as informações migradas para a corporação Alimentos Estrela.

## 🚫 CENÁRIOS NEGATIVOS  
### CT-03: Acesso a dados de corporação não migrada
**Dado que** a versão do APP está apontando para HOMOLOGAÇÃO  
**Quando** o usuário tenta acessar dados de uma corporação que não está na lista de migração  
**Então** o sistema deve mostrar uma mensagem de erro informando que os dados não estão disponíveis.

### CT-04: Validação de dados após atualização do APP
**Dado que** a versão do APP foi atualizada no dia 16/09/2025  
**Quando** o usuário acessa os dados migrados das corporações  
**Então** o sistema deve garantir que todos os dados exibidos são consistentes e correspondem aos dados migrados.

## 🔍 CENÁRIOS DE BORDA/REGRESSÃO
### CT-05: Verificação de integridade dos dados migrados
**Dado que** os dados migrados foram gerados no dia 01/08/2025  
**Quando** o usuário realiza uma consulta em qualquer uma das 5 corporações piloto  
**Então** o sistema deve validar que não há quebras ou inconsistências nos dados apresentados em relação aos dados migrados.

---

## 📝 NOTAS PARA O TESTADOR
1. Execute os cenários na ordem sugerida
2. Valide tanto frontend quanto backend quando aplicável
3. Documente qualquer desvio encontrado
4. Atualize status no Jira após execução

*Gerado automaticamente pelo QA Automation Tool*
