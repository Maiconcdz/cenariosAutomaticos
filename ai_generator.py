import os
from openai import OpenAI

class TestScenarioGenerator:
    def __init__(self):
        # Use sua NOVA chave OpenAI aqui
        api_key = os.getenv("OPENAI_API_KEY") or "SUA_NOVA_CHAVE_OPENAI_AQUI"
        self.client = OpenAI(api_key=api_key)
    
    def generate(self, key, summary, description):
        prompt = f"""
Você é um QA Sênior da Agriness, especialista em sistemas agro (Swine e Poultry).

# CONTEXTO
Estamos gerando cenários de teste para a equipe de QA da Presence/GOFarmer.

# TAREFA
Gere cenários de teste FUNCIONAIS baseados STRITAMENTE na issue abaixo.

# FORMATO OBRIGATÓRIO (BDD - Gherkin)
Use APENAS este formato:

## 🎯 CENÁRIOS POSITIVOS
### CT-01: [Nome descritivo]
**Dado que** [contexto/estado do sistema]
**Quando** [ação do usuário/sistema]
**Então** [resultado esperado]

## 🚫 CENÁRIOS NEGATIVOS  
### CT-02: [Nome descritivo]
**Dado que** [contexto]
**Quando** [ação que causa erro]
**Então** [sistema deve mostrar mensagem/comportamento]

## 🔍 CENÁRIOS DE BORDA/REGRESSÃO
### CT-03: [Nome descritivo]
**Dado que** [condição especial]
**Quando** [ação específica]
**Então** [validação de não quebra]

## 📋 DADOS DA ISSUE
**ID:** {key}
**Título:** {summary}
**Descrição/Critérios de Aceite:**
{description if description else "Sem descrição detalhada"}

# REGRAS
1. Baseie-se APENAS nos critérios fornecidos
2. Use linguagem técnica de QA
3. Considere tanto frontend quanto backend
4. Inclua validações de erro quando aplicável
5. Mantenha foco em testabilidade

Gere entre 3-5 cenários totais.
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system", 
                        "content": "Você é um QA Sênior que escreve cenários de teste claros e executáveis no padrão BDD."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1500
            )
            
            return self._format_response(key, summary, response.choices[0].message.content)
            
        except Exception as e:
            return self._generate_fallback(key, summary, description, str(e))
    
    def _format_response(self, key, summary, content):
        """Formata a resposta no padrão do time"""
        return f"""# 🧪 CENÁRIOS DE TESTE - {key}

**Título:** {summary}
**Data de geração:** {self._get_timestamp()}

---

{content}

---

## 📝 NOTAS PARA O TESTADOR
1. Execute os cenários na ordem sugerida
2. Valide tanto frontend quanto backend quando aplicável
3. Documente qualquer desvio encontrado
4. Atualize status no Jira após execução

*Gerado automaticamente pelo QA Automation Tool*
"""
    
    def _generate_fallback(self, key, summary, description, error):
        """Gera um fallback se a IA falhar"""
        return f"""# ⚠️ CENÁRIOS DE TESTE - {key} (FALLBACK)

**Título:** {summary}
**Erro na geração:** {error[:100]}

## 📋 CENÁRIOS BÁSICOS SUGERIDOS

### 1. Teste de Funcionalidade Principal
**Dado que** o sistema está configurado corretamente
**Quando** executar a funcionalidade descrita
**Então** o sistema deve comportar-se conforme especificado

### 2. Validação de Dados de Entrada
**Dado que** há dados disponíveis para processamento
**Quando** fornecer dados válidos
**Então** o sistema deve processar e retornar resultado correto

### 3. Tratamento de Erros
**Dado que** o sistema está operacional
**Quando** ocorrer uma condição de erro
**Então** o sistema deve tratar adequadamente e informar o usuário

## 📝 DESCRIÇÃO ORIGINAL
{description if description else "Sem descrição detalhada"}

---

*Cenários gerados manualmente devido a erro na automação*
"""
    
    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M")