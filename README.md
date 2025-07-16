# Sistema Bancário Simples em Python
### Projeto proposto durante o Bootcamp "Santander 2025 - Back-End com Python"
---

Este documento descreve a evolução de um **projeto simples de sistema bancário em Python**, destacando as funcionalidades da primeira versão e as melhorias implementadas posteriormente.

---

## 🔖 Versão 1: Funcionalidades Iniciais

A primeira versão do sistema oferece um **menu interativo via terminal**, permitindo que o usuário escolha entre quatro opções:

### Opções Disponíveis:
- **[d] Depositar:** Permite ao usuário informar um valor positivo para ser depositado.
- **[s] Sacar:** Permite realizar um saque, respeitando as seguintes regras:
  - Valor do saque não pode ultrapassar **R$500 por saque**.
  - Limite de **3 saques diários**.
  - Valor do saque não pode ser maior que o saldo.
- **[e] Extrato:** Exibe o histórico de movimentações realizadas e o saldo atual.
- **[q] Sair:** Finaliza o programa.

### Validações Implementadas:
- Validação de valores positivos para depósito e saque.
- Restrição quanto ao saldo, limite de saque e quantidade de saques.
- Exibição de mensagem de erro para operações inválidas.

---

## 📅 Versão 2: Funcionalidades Adicionadas

Para deixar o sistema mais robusto e próximo de uma aplicação real, duas melhorias foram implementadas:

### 1. 🌐 Saldo Inicial Personalizado
- Ao iniciar o programa, o usuário define um **saldo inicial** para sua conta.
- Simula a experiência de criação de conta bancária com um valor inicial.

### 2. ⏰ Registro de Data e Hora nas Movimentações
- Cada depósito ou saque registrado no extrato inclui a **data e hora exata** da operação.
- Gera um extrato mais completo e profissional.

### Exemplo de Registro no Extrato:
    15/07/2025 10:30:45 - Depósito: R$ 150.00

    15/07/2025 11:00:12 - Saque: R$ 50.00


---

## ✅ Benefícios das Melhorias

- **Personalização:** O usuário inicia a conta com um saldo definido por ele.
- **Transparência:** O registro com data e hora confere mais confiabilidade ao histórico de transações.
- **Experiência Realista:** As funcionalidades simulam operações básicas de um sistema bancário real.

---

## 🚀 Possíveis Melhorias Futuras
- Implementação de transferências entre contas.
- Cálculo de rendimento sobre o saldo (simulando poupança).
- Limitação de saques diários baseada em data.
- Geração de relatório de extrato em arquivo de texto ou PDF.

---

> Este projeto, apesar de simples, é um excelente exercício prático para quem está iniciando em Python e deseja aprender sobre estrutura de controle, laços de repetição, condições e manipulação de dados.
