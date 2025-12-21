"""
Gerador de Cenários de Teste - Versão Local
Não precisa de OpenAI - gera cenários baseados em templates
"""

import json
from datetime import datetime

class GeradorCenarios:
    def __init__(self):
        self.templates = {
            "Tarefa": self.gerar_tarefa,
            "Improvement": self.gerar_melhoria,
            "Incident": self.gerar_incidente,
            "Defeito": self.gerar_defeito,
            "Débito Técnico": self.gerar_debito_tecnico
        }
    
    def gerar_tarefa(self, key, summary, description):
        return f"""# 📋 Cenários de Teste - {key}
**Título:** {summary}

## 🎯 Cenários Positivos
1. **Cenário:** Execução principal conforme especificado
   - **Pré-condição:** Sistema configurado corretamente
   - **Passos:** {self.extrair_passos(description)}
   - **Resultado esperado:** Funcionalidade opera conforme especificado

2. **Cenário:** Validação de dados de entrada
   - **Pré-condição:** Dados válidos disponíveis
   - **Passos:** Inserir dados nos formatos suportados
   - **Resultado esperado:** Sistema aceita e processa dados corretamente

## 🚫 Cenários Negativos
1. **Cenário:** Dados inválidos ou incompletos
   - **Pré-condição:** Sistema em estado inicial
   - **Passos:** Inserir dados fora do padrão especificado
   - **Resultado esperado:** Sistema rejeita com mensagem de erro clara

2. **Cenário:** Exceder limites estabelecidos
   - **Pré-condição:** Sistema com dados pré-existentes
   - **Passos:** Tentar operação além dos limites
   - **Resultado esperado:** Sistema impede operação ou alerta sobre limite

## 🔍 Casos de Borda
1. **Cenário:** Campos em branco
2. **Cenário:** Valores mínimos/máximos
3. **Cenário:** Concorrência de acesso

---
*Gerado automaticamente em {datetime.now().strftime("%d/%m/%Y %H:%M")}*
"""
    
    def gerar_melhoria(self, key, summary, description):
        return f"""# 🔧 Cenários de Teste - {key}
**Tipo:** Melhoria
**Título:** {summary}

## 🧪 Testes de Aceitação
1. **Funcionalidade melhorada funciona conforme esperado**
2. **Não quebra funcionalidades existentes (regressão)**
3. **Performance mantida ou melhorada**

## 📊 Métricas de Validação
- Tempo de resposta
- Uso de recursos
- Compatibilidade com versões anteriores

---
*Gerado automaticamente em {datetime.now().strftime("%d/%m/%Y %H:%M")}*
"""
    
    def extrair_passos(self, descricao):
        """Extrai passos básicos da descrição"""
        if not descricao:
            return "Seguir fluxo padrão da aplicação"
        
        # Simplifica para demonstração
        passos = []
        if "Como um" in descricao and "Eu quero" in descricao:
            passos.append("1. Acessar funcionalidade como usuário apropriado")
            passos.append("2. Executar ação principal descrita")
            passos.append("3. Verificar resultado esperado")
        else:
            passos.append("1. Preparar ambiente de teste")
            passos.append("2. Executar funcionalidade")
            passos.append("3. Validar resultados")
        
        return "\n   ".join(passos)
    
    def gerar(self, key, summary, description, issue_type):
        generator = self.templates.get(issue_type, self.gerar_tarefa)
        return generator(key, summary, description)

# ============================================

from jira_client import JiraClient

def main():
    print("🚀 GERADOR DE CENÁRIOS DE TESTE - PRESENCE")
    print("="*60)
    
    try:
        # Conecta ao Jira
        jira = JiraClient()
        gerador = GeradorCenarios()
        
        # Busca issues
        print("\n🔎 Buscando issues do board...")
        issues = jira.get_board_issues(limit=5)
        
        print(f"✅ {len(issues)} issues encontradas!")
        
        # Filtra tipos relevantes
        tipos_validos = ["Tarefa", "Improvement", "Incident", "Defeito"]
        
        for issue in issues:
            key = issue["key"]
            fields = issue["fields"]
            issue_type = fields.get("issuetype", {}).get("name", "Tarefa")
            
            if issue_type not in tipos_validos:
                print(f"⏭️  Pulando {key} - Tipo: {issue_type}")
                continue
            
            summary = fields.get("summary", "")
            description = fields.get("description", "")
            
            print(f"\n📋 Processando: {key} ({issue_type})")
            print(f"   {summary[:60]}...")
            
            # Gera cenários
            cenarios = gerador.gerar(key, summary, description, issue_type)
            
            # Salva arquivo
            filename = f"CENARIOS_{key}.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(cenarios)
            
            print(f"✅ Salvo: {filename}")
        
        print(f"\n{'='*60}")
        print("🎉 GERAÇÃO CONCLUÍDA!")
        print(f"{'='*60}")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()