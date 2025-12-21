# 📋 CENÁRIOS DE TESTE - PRESENCE-3010

**Título:** [ANÁLISE] - Homologação dos dados migrados (presence - bff)
**Gerado em:** 17/12/2025 16:09
**Status:** Geração manual (API indisponível)

---

## 🎯 CENÁRIOS BÁSICOS

### CT-01: Validação funcional principal
**Dado que** o sistema está configurado e acessível
**Quando** executar a funcionalidade conforme especificado
**Então** o sistema deve comportar-se conforme os critérios de aceite

### CT-02: Teste com dados válidos
**Dado que** existem dados de entrada no formato correto
**Quando** submeter os dados para processamento
**Então** o sistema deve processar e retornar resultado esperado

### CT-03: Tratamento de erros e validações
**Dado que** o sistema está operacional
**Quando** fornecer dados inválidos ou realizar ação incorreta
**Então** o sistema deve exibir mensagem de erro clara e impedir a operação

---

## 📄 INFORMAÇÕES DA TASK

**Descrição original:**
Validar os dados migrados de Presence e Corp para as 5 corporações piloto *em homologação*:

Versão do APP apontando para HOMOLOGAÇÃO, na qual foi gerada no dia 01/08/2025 e teve uma atualização no dia 16/09/2025.

h2. CORPORAÇÕES:

||*HOLDING_UUID*||*NOME HOLDING /  PROPRIEDADE*||
|{{2c31715d-0c01-40e7-a590-3e0c00073aa6}}|COPÉRDIA|
|{{20505c4e-96c0-4746-a30e-dbef949341e2}}|Alimentos Estrela|
|{{4719b746-e10e-41a5-ac51-a07e484570fb}}|Castrolanda Leite|
|{{071c638d-bb9b-4e68-a5d1-416da57d887f}}|SSA - São Salvador Alimentos - Aves de Corte|
|{{6179f042-e159-499a-98fb-21798669e58f}}|Aurora Poultry|

* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3981377628/Corpora+es|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3981377628/Corpora+es|smart-link] 
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3944120322/T+cnicos|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3944120322/T+cnicos|smart-link]  {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3980951608/Produtores|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3980951608/Produtores|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3981312066/Regi+es|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3981312066/Regi+es|smart-link]  {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4078043137/Granjas|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4078043137/Granjas|smart-link]  {color:#36B37E}*[ DONE ]*{color} (!) Problema no retorno das consultas ([Problema|https://agriness-team.atlassian.net/browse/PLAT-2183?focusedCommentId=247770])
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943235614/Tipos+de+atendimento|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943235614/Tipos+de+atendimento|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943071763/Checklists|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943071763/Checklists|smart-link] {color:#36B37E}*[ DONE ]*{color} (!) Problema no retorno das consultas ([Problema|https://agriness-team.atlassian.net/browse/PLAT-2183?focusedCommentId=247832])
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943137313/Itens+de+checklist|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943137313/Itens+de+checklist|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3944218628/Solicita+es+de+visita+da+granja|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3944218628/Solicita+es+de+visita+da+granja|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943694370/Solicita+es+de+visita+do+lote|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943694370/Solicita+es+de+visita+do+lote|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3944120347/Agendamentos+de+visita+t+cnica|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3944120347/Agendamentos+de+visita+t+cnica|smart-link] {color:#36B37E}*[ DONE ]*{color} (!)  Problema no retorno das consultas ([Problema|https://agriness-team.atlassian.net/browse/PLAT-2183?focusedCommentId=248346])
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943366684/Visita+t+cnica|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943366684/Visita+t+cnica|smart-link] {color:#36B37E}*[ DONE ]*{color} (!) Problema no retorno das consultas ([Problema|https://agriness-team.atlassian.net/browse/PLAT-2183?focusedCommentId=248541])
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943366694/Aplica+es+de+checklist+de+granja|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943366694/Aplica+es+de+checklist+de+granja|smart-link] {color:#36B37E}*[ DONE ]*{color} (!) Atenção ao [Comentário|https://agriness-team.atlassian.net/browse/PLAT-2183?focusedCommentId=248605].
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4298768395/Aplica+es+de+itens+de+checklist+de+granja|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4298768395/Aplica+es+de+itens+de+checklist+de+granja|smart-link] {color:#36B37E}*[ DONE ]*{color}  Problema no retorno das consultas ([problema|https://agriness-team.atlassian.net/browse/PLAT-2183?focusedCommentId=248686])
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3944710145/Aplica+es+de+checklist+de+lote|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3944710145/Aplica+es+de+checklist+de+lote|smart-link] {color:#36B37E}*[ DONE ]*{color} Problema no retorno das consultas ([Problema|https://agriness-team.atlassian.net/browse/PLAT-2183?focusedCommentId=248745])
*  [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4298932364/Aplica+es+de+itens+de+checklist+do+lote|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4298932364/Aplica+es+de+itens+de+checklist+do+lote|smart-link] {color:#36B37E}*[ DONE ]*{color} Problema no retorno das Consultas. ([Problema|https://agriness-team.atlassian.net/browse/PLAT-2183?focusedCommentId=249008])
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4304666625/Risco+Sanit+rio|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4304666625/Risco+Sanit+rio|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3945201665/Notas+e+recomenda+es+t+cnicas+da+granja|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3945201665/Notas+e+recomenda+es+t+cnicas+da+granja|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3945332772/Notas+e+recomenda+es+t+cnicas+do+lote|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3945332772/Notas+e+recomenda+es+t+cnicas+do+lote|smart-link] {color:#36B37E}*[ DONE ]*{color} [Atenção.|https://agriness-team.atlassian.net/browse/PLAT-2183?focusedCommentId=249193] ao comentário.
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3945136140/Notas+de+atendimento+sem+produtor|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3945136140/Notas+de+atendimento+sem+produtor|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943104563/Quil+metros+rodados|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/3943104563/Quil+metros+rodados|smart-link] {color:#36B37E}*[ DONE ]*{color} ([Problema|https://agriness-team.atlassian.net/browse/PLAT-2183?focusedCommentId=249617])
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4042063874/Autoriza+es+de+aplica+o+de+checklist|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4042063874/Autoriza+es+de+aplica+o+de+checklist|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4045963265/Regras+de+pagamento+de+lote|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4045963265/Regras+de+pagamento+de+lote|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4053729303/Configura+es+de+par+metros+de+produ+o+da+plataforma|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4053729303/Configura+es+de+par+metros+de+produ+o+da+plataforma|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4049436697/Configura+es+de+par+metros+de+produ+o+da+corpora+o|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4049436697/Configura+es+de+par+metros+de+produ+o+da+corpora+o|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4054220801/Configura+es+de+controle+de+visualiza+o+de+plataforma|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4054220801/Configura+es+de+controle+de+visualiza+o+de+plataforma|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4054581249/Configura+es+de+controle+de+visualiza+o+de+corpora+o|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4054581249/Configura+es+de+controle+de+visualiza+o+de+corpora+o|smart-link] {color:#36B37E}*[ DONE ]*{color}
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4068835329/Regras+de+bloqueio+conf.+controle+de+uso|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4068835329/Regras+de+bloqueio+conf.+controle+de+uso|smart-link] {color:#36B37E}*[ DONE ]*{color} Problema no retorno da Consulta ([Problema|https://agriness-team.atlassian.net/browse/PLAT-2183?focusedCommentId=249861])
* [https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4085481473/Acertos+de+lote|https://agriness-team.atlassian.net/wiki/spaces/SS/pages/4085481473/Acertos+de+lote|smart-link] {color:#36B37E}*[ DONE ]*{color}

---

⚠️ *Cenários gerados manualmente - Recomenda-se revisão detalhada*
