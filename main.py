import os
import sys
from jira_client import JiraClient
from ai_generator import TestScenarioGenerator
from datetime import datetime

def setup_environment():
    """Configura variáveis de ambiente"""
    # SUA NOVA CHAVE OPENAI AQUI
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    
    # Cria estrutura de pastas
    os.makedirs("cenarios_sprint", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

def log_message(message):
    """Registra mensagens no log"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    
    print(log_line)
    
    # Salva em arquivo
    with open("logs/execucao.log", "a", encoding="utf-8") as f:
        f.write(log_line + "\n")

def main():
    # Configuração
    MAX_ISSUES = 5  # Máximo de issues para processar
    
    print(f"""
    {'='*70}
    🚀 QA AUTOMATION - GERADOR DE CENÁRIOS DE TESTE
    {'='*70}
    Sistema: Presence/GOFarmer
    Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
    {'='*70}
    """)
    
    # Setup
    setup_environment()
    log_message("Iniciando execução do gerador de cenários")
    
    try:
        # Inicializa clientes
        log_message("Conectando ao Jira...")
        jira = JiraClient()
        
        log_message("Configurando gerador de cenários...")
        ai = TestScenarioGenerator()
        
        # Busca issues da sprint atual
        log_message("Buscando issues da sprint ativa...")
        issues = jira.get_issues_from_active_sprint(limit=MAX_ISSUES)
        
        if not issues:
            log_message("Nenhuma issue encontrada para teste")
            print("\n❌ Nenhuma issue encontrada na sprint atual")
            print("   Verifique se há issues com tipos: Tarefa, Melhoria, Improvement")
            sys.exit(0)
        
        log_message(f"Encontradas {len(issues)} issues para processar")
        
        # Processa cada issue
        resultados = []
        for i, issue in enumerate(issues, 1):
            print(f"\n{'='*70}")
            print(f"📋 ISSUE {i}/{len(issues)}")
            print(f"{'='*70}")
            
            key = issue["key"]
            fields = issue["fields"]
            
            issue_type = fields.get("issuetype", {}).get("name", "Desconhecido")
            status = fields.get("status", {}).get("name", "Desconhecido")
            summary = fields.get("summary", "Sem título")
            description = fields.get("description", "Sem descrição") or "Sem descrição detalhada"
            
            print(f"📍 ID: {key}")
            print(f"🏷️  Tipo: {issue_type}")
            print(f"📈 Status: {status}")
            print(f"📝 Título: {summary}")
            
            if description != "Sem descrição detalhada":
                print(f"📄 Descrição: {description[:150]}...")
            
            # Gera cenários
            print(f"\n🧪 Gerando cenários de teste...")
            try:
                scenarios = ai.generate(key, summary, description)
                
                # Salva arquivo
                filename = f"cenarios_sprint/{key}_cenarios.md"
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(scenarios)
                
                print(f"✅ Arquivo salvo: {filename}")
                resultados.append((key, filename, "SUCESSO"))
                
                # Mostra amostra
                print(f"\n📄 Amostra dos cenários:")
                lines = scenarios.split('\n')
                for line in lines[:8]:
                    if line.strip():
                        print(f"   {line}")
                if len(lines) > 8:
                    print(f"   ... ({len(lines)-8} linhas restantes)")
                
            except Exception as e:
                error_msg = f"Erro em {key}: {str(e)[:100]}"
                print(f"❌ {error_msg}")
                log_message(error_msg)
                resultados.append((key, "", f"ERRO: {e}"))
        
        # Relatório final
        print(f"\n{'='*70}")
        print("📊 RELATÓRIO DE EXECUÇÃO")
        print(f"{'='*70}")
        
        sucessos = [r for r in resultados if "SUCESSO" in r[2]]
        erros = [r for r in resultados if "ERRO" in r[2]]
        
        print(f"✅ Sucessos: {len(sucessos)}")
        print(f"❌ Erros: {len(erros)}")
        print(f"📁 Pasta: cenarios_sprint/")
        print(f"⏰ Tempo total: {datetime.now().strftime('%H:%M:%S')}")
        
        if sucessos:
            print(f"\n📄 Arquivos gerados:")
            for key, filename, _ in sucessos:
                print(f"   • {key} → {filename}")
        
        print(f"\n{'='*70}")
        print("🎉 PROCESSO CONCLUÍDO COM SUCESSO!")
        print(f"{'='*70}")
        
        log_message(f"Execução concluída: {len(sucessos)} sucessos, {len(erros)} erros")
        
    except Exception as e:
        error_msg = f"ERRO CRÍTICO: {str(e)}"
        print(f"\n💥 {error_msg}")
        log_message(error_msg)
        sys.exit(1)

if __name__ == "__main__":
    main()