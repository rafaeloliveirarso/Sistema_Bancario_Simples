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
```
15/07/2025 10:30:45 - Depósito: R$ 150.00
15/07/2025 11:00:12 - Saque: R$ 50.00
```

---

## 🛠️ Versão 3: Modularização e Novas Funcionalidades

Nesta nova etapa, o sistema foi **refatorado e modularizado** com o objetivo de tornar o código mais organizado, reutilizável e próximo de um sistema bancário real.

### 🗂️ Funções Criadas:
- **sacar:** Operação de saque com parâmetros nomeados.
- **depositar:** Operação de depósito com parâmetros posicionais.
- **exibir_extrato:** Exibição do extrato combinando parâmetros posicionais e nomeados.
- **criar_usuario:** Cadastro de novo cliente com CPF único.
- **criar_conta:** Criação de conta vinculada ao usuário existente.
- **listar_contas:** Lista todas as contas cadastradas com informações do titular.

### 📌 Regras Adicionais:
- O CPF do usuário deve ser único.
- O número da conta é sequencial e a agência é fixa (0001).
- Um usuário pode ter múltiplas contas.

### 📋 Exemplo de Uso:

- Criar usuário informando nome, data de nascimento, CPF e endereço.
- Criar conta informando o CPF do usuário.
- Realizar depósitos, saques e consultar o extrato.
- Listar todas as contas criadas no sistema.

---

## ✅ Benefícios das Melhorias

- **Organização:** Código modular facilita manutenção e futuras melhorias.
- **Controle:** Cadastro de usuários e contas permite controle sobre múltiplas contas.
- **Histórico:** Extrato completo com movimentações detalhadas.
- **Escalabilidade:** Sistema pronto para receber futuras implementações como transferências ou geração de relatórios.

---

## 🚀 Possíveis Melhorias Futuras

- Implementação de transferências entre contas.
- Cálculo de rendimento sobre o saldo (simulando poupança).
- Limitação de saques diários baseada em data.
- Geração de relatório de extrato em arquivo de texto ou PDF.
- Autenticação de usuários.

---

> Este projeto, apesar de simples, é um excelente exercício prático para quem está iniciando em Python e deseja aprender sobre estrutura de controle, funções, parâmetros, listas e manipulação de dados.