# Automação SysOS x GitHub 🚀

Ambiente oficial de testes, homologação e auditoria da integração entre o **SysOS** e o **GitHub Projects**.

Aqui são validados todos os disparos automáticos de Ordens de Serviço (OS), tarefas dos desenvolvedores, movimentação de cards e controle de status.

---

## 📌 Como a automação funciona?

Tudo o que acontece dentro do SysOS reflete em tempo real no GitHub:

1. **Criou uma OS no SysOS** ➔ O sistema cria uma Issue aqui e coloca o card no GitHub Projects na coluna **Backlog** com a label `workflow::backlog`.
2. **Iniciou uma Tarefa (Play)** ➔ O card da OS vai automaticamente para **Em Desenvolvimento** (`workflow::desenvolvimento`).
3. **Pausou a Tarefa (Pause)** ➔ O card vai para **Pausada** ou volta para a fila correspondente.
4. **Finalizou a Tarefa (Stop)** ➔ O checklist daquela tarefa é marcado como concluído `[x]`. Se for a última tarefa da OS, o card é movido para **Em Testes** (`workflow::testes`).
5. **Reatribuiu para outro Desenvolvedor** ➔ O responsável (`assignee`) da Issue é atualizado e um comentário de histórico é registrado.
6. **Reprovou a OS no Teste** ➔ O card é movido para **Reprovada / Correção** (`tipo::correcao`) com o comentário da justificativa preenchida pelo testador.
7. **Aprovou a OS no Teste** ➔ O card é movido para **Homologação** (`workflow::homologacao`).
8. **Gerou Release / Versão em Produção** ➔ A Issue é fechada como concluída (`workflow::concluido`).

---

## 🏷️ Mapeamento de Labels

O repositório está configurado com 16 labels organizadas em grupos simples:

| Grupo | Labels | Finalidade |
| :--- | :--- | :--- |
| **Prioridade** | `prioridade::baixa`, `prioridade::media`, `prioridade::alta`, `prioridade::critica` | Nível de urgência definido na abertura da OS |
| **Tipo** | `tipo::funcionalidade`, `tipo::melhoria`, `tipo::correcao`, `tipo::tarefa-tecnica` | Natureza da demanda |
| **Workflow** | `workflow::backlog`, `workflow::analise`, `workflow::pronto`, `workflow::desenvolvimento`, `workflow::revisao`, `workflow::testes`, `workflow::homologacao`, `workflow::concluido` | Fase atual do ciclo de vida |

---

## 📂 Estrutura do Repositório

```text
automacao-sysos/
├── docs/
│   ├── FLUXO_OS_TAREFAS.md      # Passo a passo de cada tela do SysOS
│   └── LABELS_E_COLUNAS.md      # Tabela detalhada das 16 labels e cores
├── auditoria/
│   └── RELATORIO_STATUS_AUTOMACAO.md # Diagnóstico e melhorias em andamento
├── logs/                        # Registros de eventos e auditorias de teste
└── scripts/
    └── simular_evento_os.py     # Script para simular eventos de OS e tarefas
```

---

## ⚙️ Regras do Ambiente de Teste

- Este repositório serve para testar e validar o código antes de promover para a organização principal (`Neeo-Projetos`).
- Os testes validam tanto o envio de dados via REST/GraphQL quanto a resiliência a quedas de conexão ou falhas de token.
