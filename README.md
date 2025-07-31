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

### 2. ⏰ Registro de Data e Hora nas Movimentações
- Cada depósito ou saque registrado no extrato inclui a **data e hora exata** da operação.

### Exemplo de Registro no Extrato:
    15/07/2025 10:30:45 - Depósito: R$ 150.00
    15/07/2025 11:00:12 - Saque: R$ 50.00


---

## 🛠️ Versão 3: Modularização e Novas Funcionalidades

Nesta nova etapa, o sistema foi **refatorado e modularizado** com o objetivo de tornar o código mais organizado, reutilizável e próximo de um sistema bancário real.

### 🗂️ Funções Criadas:
- **sacar**
- **depositar**
- **exibir_extrato**
- **criar_usuario**
- **criar_conta**
- **listar_contas**

### 📌 Regras Adicionais:
- O CPF do usuário deve ser único.
- O número da conta é sequencial.
- A agência é fixa: `0001`.
- Um usuário pode ter múltiplas contas.

---

## 🧱 Versão 4: Refatoração Completa com Programação Orientada a Objetos (POO)

Nesta versão, o projeto foi completamente reestruturado utilizando os conceitos de **POO**, tornando o código mais escalável, organizado e alinhado com boas práticas de desenvolvimento.

### 🔧 Classes Criadas:

#### 📦 `Conta`
- Atributos: `saldo`, `número`, `agência`, `cliente`, `histórico`
- Métodos: `sacar()`, `depositar()`

#### 🏦 `ContaCorrente` (herda de `Conta`)
- Atributos: `limite`, `limite_saques`, `quantidade_saques`

#### 🧾 `Historico`
- Armazena todas as transações realizadas.
- Método: `adicionar_transacao(transacao)`

#### 🔁 `Transacao` (classe abstrata)
- Subclasses: `Saque`, `Deposito`
- Método abstrato: `registrar(conta)`

#### 👤 `Cliente`
- Atributo: `endereco`
- Método: `adicionar_conta(conta)`

#### 🧍 `PessoaFisica` (herda de `Cliente`)
- Atributos: `nome`, `cpf`, `data_nascimento`

---

### 🔄 Operações do Menu Atualizadas:
- **[d] Depositar** → Utiliza a classe `Deposito`
- **[s] Sacar** → Utiliza a classe `Saque` com controle de limite e quantidade
- **[e] Extrato** → Usa a classe `Historico` da conta
- **[nu] Novo usuário** → Cria instância de `PessoaFisica`
- **[nc] Nova conta** → Cria `ContaCorrente` vinculada ao cliente
- **[lc] Listar contas** → Mostra contas com nome e CPF do titular

---

## ✅ Benefícios da Versão 4 com POO

- **Encapsulamento:** A lógica foi distribuída entre as classes corretas.
- **Reutilização:** Métodos comuns foram herdados de superclasses.
- **Extensibilidade:** Fácil adicionar novos tipos de contas, validações, regras e integrações.
- **Organização:** A separação clara de responsabilidades melhora a legibilidade e manutenção.

---

## 📁 Exemplo de Estrutura Atual:

.
├── banco.py\
├── models\
│ ├── conta.py\
│ ├── cliente.py\
│ ├── historico.py\
│ └── transacoes.py\
└── main.py\


---

## 🚀 Possíveis Melhorias Futuras

- Interface gráfica com Tkinter ou PyQT
- Banco de dados para persistência de clientes e contas
- Integração com API REST (Flask ou FastAPI)
- Autenticação de usuário com login/senha
- Testes unitários com pytest

---

> Este projeto evoluiu de um script simples até um sistema orientado a objetos, sendo ideal para quem deseja aprender desde os fundamentos até conceitos mais avançados de Python e POO.
