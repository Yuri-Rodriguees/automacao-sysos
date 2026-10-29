# Fluxo Completo: SysOS ➔ GitHub 🔄

Guia direto explicando o comportamento da automação em cada tela do SysOS.

---

## 1. Cadastro de Ordem de Serviço (`cadastro_ordemServico.php`)

- **Ação:** Usuário preenche a OS (Solicitante, Nome, Objetivo, Requisitos, Imagens, Equipe) e clica em **Gravar**.
- **Comportamento:**
  - O SysOS grava a OS no SQL Server (`sysos.ordemServico`).
  - A automação gera o card no GitHub com título `#NUMERO - Titulo` (ou prefixo `HU-XXXX`, `ME-XXXX`).
  - O corpo da Issue recebe:
    - Informações gerais da OS;
    - Requisitos funcionais e não funcionais;
    - Lista de anexos e imagens salvas;
    - Checklist com as tarefas planejadas (`- [ ] Tarefa`);
    - Desenvolvedor responsável definido em `assignees`.
  - O card entra no projeto na coluna **Backlog** (`workflow::backlog`).
  - O número da Issue e o node ID são gravados na tabela `sysos.ordemServicoGithub`.

---

## 2. Planejamento de Tarefas (`cadastro_ordemServicoTarefa.php`)

- **Ação:** Inclusão de novas tarefas, alteração de prazos ou reatribuição de desenvolvedor (`realizadorTarefa`).
- **Comportamento:**
  - O checklist da Issue no GitHub é atualizado.
  - Se um novo desenvolvedor for definido, a Issue atualiza os responsáveis (`assignees`).

---

## 3. Controle de Tarefas do Desenvolvedor (`cadastro_controleDeTarefas.php`)

### A. Iniciar Tarefa (Botão Play)
- **Status Tarefa:** `1` (Em Andamento).
- **Ação no GitHub:** Card movido para **Em Desenvolvimento** (`workflow::desenvolvimento`).

### B. Pausar Tarefa (Botão Pause)
- **Status Tarefa:** `3` (Pausada).
- **Ação no GitHub:** Card movido para **Pausada**.

### C. Finalizar Tarefa (Botão Stop)
- **Status Tarefa:** `2` (Finalizada).
- **Ação no GitHub:**
  - A tarefa específica é marcada como concluída no checklist (`- [x] Tarefa`).
  - Se ainda existirem tarefas pendentes: o card continua em desenvolvimento.
  - Se for a **última tarefa**: o desenvolvedor preenche as considerações finais e tabelas/procedures alteradas, e a OS vai para **Em Testes** (`workflow::testes`).

---

## 4. Teste e Homologação (`cadastro_ordemServicoFiltro.php`)

### A. Reprovação
- **Ação:** Testador clica em "Reprovar" e informa o motivo.
- **Ação no GitHub:**
  - Card movido para **Reprovada / Correção** (`tipo::correcao`).
  - Comentário automático adicionado na Issue:
    ```markdown
    ## ❌ OS Reprovada
    > **Justificativa:** [Motivo digitado pelo testador]
    ---
    🤖 Atualização automática pelo Sistema de OS
    ```

### B. Aprovação
- **Ação:** Testador clica em "Aprovar".
- **Ação no GitHub:** Card movido para **Homologação** (`workflow::homologacao`).

---

## 5. Liberação e Versão Oficial (`cadastro_ordemServicoVersao.php`)

- **Ação:** A versão de produção é gerada com o pacote de OSs aprovadas.
- **Ação no GitHub:**
  - A Issue é fechada (`state: closed`).
  - O card é movido para a coluna **Concluído** (`workflow::concluido`).
