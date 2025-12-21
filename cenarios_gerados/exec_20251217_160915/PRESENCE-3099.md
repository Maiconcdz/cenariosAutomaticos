# 📋 CENÁRIOS DE TESTE - PRESENCE-3099

**Título:** [APP] - Análise de consumo de ração - Consumo por carga, por tipo e por grupo de ração
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
*Objetivo*

Essa demanda é a continuação da [https://agriness-team.atlassian.net/browse/PRESENCE-2626|https://agriness-team.atlassian.net/browse/PRESENCE-2626|smart-link] , onde nessa demanda deve ser desenvolvida os outros 3 agrupadores.

||*Consumo por carga de ração*||*Consumo por ração (tipo)*||*Consumo por grupo*||
|!image-20250919-162839.png|width=325,height=441,alt="image-20250919-162839.png"!|!image-20250919-162912.png|width=329,height=442,alt="image-20250919-162912.png"!|!image-20250919-163023.png|width=318,height=445,alt="image-20250919-163023.png"!|
|*consumptionsPerLoad*
* Nome da ração: {{name}}
* Período: {{startDate}} e {{finalDate}}
* CMD Real: {{cmdReal}}
* CMD Previsto: {{cmdPlanned}}
* Diferença: {{cmdDiff}}
* Consumo Ração/Cab: {{cmdFeed}}|*consumptionsPerType*
* Nome da ração: {{name}}
* Período: {{startDate}} e {{finalDate}}
* CMD Real: {{cmdReal}}
* CMD Previsto: {{cmdPlanned}}
* Diferença: {{cmdDiff}}
* Consumo Ração/Cab: {{cmdFeed}}|*consumptionsPerGroup*
* Nome da ração: {{name}}
* Período: {{startDate}} e {{finalDate}}
* CMD Real: {{cmdReal}}
* CMD Previsto: {{cmdPlanned}}
* Diferença: {{cmdDiff}}
* Consumo Ração/Cab: {{cmdFeed}}|

----

*Protótipo*:

[https://www.figma.com/design/Hs5rogemnw88NrauJ9AkJJpC/Presence-App?node-id=27473-106842&t=yN0EYiQ61JNc3fWd-4|https://www.figma.com/design/Hs5rogemnw88NrauJ9AkJJpC/Presence-App?node-id=27473-106842&t=yN0EYiQ61JNc3fWd-4|smart-link] 

----

*Material de Apoio:*

* Aqui a transcrição do refinamento técnico dessa demanda: [https://docs.google.com/spreadsheets/d/1RtDPpdE-edw_pu0STx07bLPf3L4tT1ZKijhcyjRuWOo/edit?gid=0#gid=0|https://docs.google.com/spreadsheets/d/1RtDPpdE-edw_pu0STx07bLPf3L4tT1ZKijhcyjRuWOo/edit?gid=0#gid=0|smart-link] 
* [https://agriness-team.atlassian.net/wiki/spaces/PRES/pages/4073881621/06.01.03.08+-+An+lise+de+consumo+de+ra+o+a+implementar|https://agriness-team.atlassian.net/wiki/spaces/PRES/pages/4073881621/06.01.03.08+-+An+lise+de+consumo+de+ra+o+a+implementar|smart-link] 

----

*Exemplo de lote para utilizar em QA com dados.* 

{noformat}HOLDING:
56891a9c-0586-4adb-8780-c02a423de438

FARM:
"uuid": "bd10638b-ba30-4a41-87c8-3ab5e5c249ac",
"name": "CLARINES CECCHIN PEREIRA Prop 1",

LOTE:
uuid: 2b959ac1-ce49-4216-b964-205bd01631b9
"name": "115695.01.01.0005 AUR"{noformat}

*CURL*: Onde devemos enviar o id da holding, id da farm e id do animal group 

{noformat}curl --location 'https://presence-bff.agriness-qa.com/api/v1/holding/56891a9c-0586-4adb-8780-c02a423de438/farm/bd10638b-ba30-4a41-87c8-3ab5e5c249ac/animal_group/2b959ac1-ce49-4216-b964-205bd01631b9/feed_consumptions_analysis' \
--header 'Authorization: eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ2R1hveGMwZGw5OWwzanQxVXdTNllpZEphWURXZ2NWZ0NkM29TZmVWZ1dRIn0.eyJleHAiOjE3NjI0NjA1OTAsImlhdCI6MTc2MjM3NDE5MCwianRpIjoiYTVlODg5YWItZjIzNS00ZjIzLWIxM2ItNWZiZjI0NmU1ZWMzIiwiaXNzIjoiaHR0cHM6Ly9pcy5hZ3JpbmVzcy1xYS5jb20vYXV0aC9yZWFsbXMvYWdyaW5lc3Mtc3RhZ2UiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMzkzNjY1NzAtOTA1ZS00ZDQxLThiMDgtOWNhNTlhZjQ4OGQ0IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoicHJlc2VuY2UiLCJzZXNzaW9uX3N0YXRlIjoiNWY2MTlkNTQtMTJkNi00MTQwLTg1NDYtNTNjZTBlODFmM2MzIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvZmZsaW5lX2FjY2VzcyIsIm5hbWUiOiJVU1XDgVJJTyBRQSBQUkVTRU5DRSBNSUdSQcOHw4NPIFNXSU5FIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicHJlc2VuY2Vfc3dpbmVAYWdyaW5lc3MuY29tIiwiZ2l2ZW5fbmFtZSI6IlVTVcOBUklPIFFBIFBSRVNFTkNFIE1JR1JBw4fDg08gU1dJTkUiLCJmYW1pbHlfbmFtZSI6IiIsImVtYWlsIjoicHJlc2VuY2Vfc3dpbmVAYWdyaW5lc3MuY29tIn0.Xz1-iw9MBQLXRl0oqQj5F3sZimsiVIR4By2k_afXz3MLH6IIdYXAzUE_-IywfHpBp7vi-oBb0jd3Z2bc4uC5PdTq2-4VP1-E5Q_4JlThitUYcAIPQmqhJWcv_XBdvxf6rVO8f2vFjvKp61Z0Y10LpGM4V95X9eoeA64HKTC5nYRsP3PCLulXihFYH1D7zpma7z_C4E8xIx4gyOxLIuP7QKWAfM5vN-en3d64VMMF0I7gKJEW3sjnIOeyUqse409Ld3b6aJu4l0rLDQGgL5GwWqFX9quNyHMo1VCDhcHgCCm9G_z5EcD5Rvoo-cYzNBAvebe1Vi2TJqkQTwKjvwm-LA'{noformat}

---

⚠️ *Cenários gerados manualmente - Recomenda-se revisão detalhada*
