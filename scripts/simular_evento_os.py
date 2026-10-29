#!/usr/bin/env python3
"""
Script de teste e simulação de eventos do SysOS para o GitHub.
Permite testar a criação de issues, adição de comentários e etiquetas sem passar pela interface gráfica.
"""

import sys
import json
import urllib.request
import urllib.error

def criar_issue_teste(token, repo_owner, repo_name, numero_os, titulo, responsavel=None):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    
    corpo = f"""## 📋 Ordem de Serviço #{numero_os} (Teste de Automação)

### ℹ️ Informações Gerais
- **Código:** #{numero_os}
- **Ambiente:** Teste de Validação SysOS
- **Tipo:** Criação
- **Prioridade:** Média

### 📋 Checklist de Tarefas
- [ ] 1. Análise técnica e modelagem de banco
- [ ] 2. Implementação das regras de negócio
- [ ] 3. Validação em ambiente de homologação

---
<sub>🤖 Issue gerada pelo script de teste da automação SysOS</sub>
"""

    payload = {
        "title": f"#{numero_os} - {titulo}",
        "body": corpo,
        "labels": ["workflow::backlog", "tipo::funcionalidade", "prioridade::media"]
    }
    
    if responsavel:
        payload["assignees"] = [responsavel]

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "SysOS-Test-Script"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            resultado = json.loads(resp.read().decode("utf-8"))
            print(f"✅ Issue #{resultado['number']} criada com sucesso: {resultado['html_url']}")
            return resultado
    except urllib.error.HTTPError as e:
        print(f"❌ Erro HTTP {e.code}: {e.read().decode('utf-8')}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Uso: python simular_evento_os.py <TOKEN> <OWNER> <REPO> <NUMERO_OS> <TITULO> [RESPONSAVEL]")
        sys.exit(1)
        
    token = sys.argv[1]
    owner = sys.argv[2]
    repo = sys.argv[3]
    numero_os = sys.argv[4]
    titulo = sys.argv[5]
    resp = sys.argv[6] if len(sys.argv) > 6 else None
    
    criar_issue_teste(token, owner, repo, numero_os, titulo, resp)
