import requests
import os
from datetime import datetime

class JiraClient:
    def __init__(self):
        self.base_url = "https://agriness-team.atlassian.net"
        self.email = os.getenv("JIRA_EMAIL")
        self.token = os.getenv("JIRA_API_TOKEN")
        
        self.auth = (self.email, self.token)
        self.headers = {"Accept": "application/json"}
    
    def get_issues_from_active_sprint(self, limit=5):
        """Busca issues da SPRINT ATIVA para teste"""
        print("🔍 Buscando SPRINT ATIVA...")
        
        # 1. Busca sprint ativa
        sprint_url = f"{self.base_url}/rest/agile/1.0/board/302/sprint"
        params = {"state": "active"}
        
        try:
            response = requests.get(
                sprint_url,
                headers=self.headers,
                auth=self.auth,
                params=params
            )
            
            if response.status_code != 200:
                print(f"❌ Erro ao buscar sprint: {response.status_code}")
                return []
            
            sprints = response.json().get("values", [])
            
            if not sprints:
                print("📭 Nenhuma sprint ativa encontrada")
                return []
            
            active_sprint = sprints[0]
            sprint_id = active_sprint["id"]
            sprint_name = active_sprint["name"]
            
            print(f"📅 Sprint ativa: {sprint_name}")
            
        except Exception as e:
            print(f"❌ Erro de conexão: {e}")
            return []
        
        # 2. Busca issues da sprint
        print(f"🔎 Buscando issues da sprint...")
        issues_url = f"{self.base_url}/rest/agile/1.0/board/302/issue"
        
        params = {
            "startAt": 0,
            "maxResults": 100,  # Busca bastante para filtrar
            "jql": f'sprint = {sprint_id}',
            "fields": "summary,description,issuetype,status,priority"
        }
        
        try:
            response = requests.get(
                issues_url,
                headers=self.headers,
                auth=self.auth,
                params=params
            )
            
            if response.status_code != 200:
                print(f"❌ Erro nas issues: {response.status_code}")
                return []
            
            data = response.json()
            all_issues = data.get("issues", [])
            
            print(f"📊 Total na sprint: {len(all_issues)} issues")
            
        except Exception as e:
            print(f"❌ Erro: {e}")
            return []
        
        # 3. Filtra issues relevantes
        print("🎯 Filtrando issues testáveis...")
        
        filtered_issues = []
        tipos_teste = ["Tarefa", "Improvement", "Melhoria", "Task", "Story", "Bug"]
        status_teste = ["To Do", "In Progress", "Em Andamento", "Pronto para Teste", "Ready for Test"]
        
        for issue in all_issues:
            fields = issue.get("fields", {})
            
            issue_type = fields.get("issuetype", {}).get("name", "")
            status = fields.get("status", {}).get("name", "")
            summary = fields.get("summary", "")
            
            # Verifica se é tipo testável E status correto
            if issue_type in tipos_teste and status in status_teste:
                # Verifica se tem descrição ou critérios
                description = fields.get("description", "")
                if description or "critério" in summary.lower() or "aceite" in summary.lower():
                    filtered_issues.append(issue)
            
            # Para se já atingiu o limite
            if len(filtered_issues) >= limit:
                break
        
        print(f"✅ {len(filtered_issues)} issues testáveis encontradas")
        return filtered_issues
    
    def get_board_issues(self, limit=5):
        """Mantém compatibilidade"""
        return self.get_issues_from_active_sprint(limit)