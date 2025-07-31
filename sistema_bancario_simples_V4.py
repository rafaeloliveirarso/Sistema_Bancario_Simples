from datetime import datetime, date

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })


class Transacao:
    def __init__(self, valor):
        self.valor = valor

    def registrar_conta(self, conta):
        raise NotImplementedError("Implementar método registrar_conta")


class Deposito(Transacao):
    def registrar_conta(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def registrar_conta(self, conta):
        if conta.pode_sacar(self.valor):
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(self)
            return True
        return False


class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def pode_sacar(self, valor):
        return self.saldo >= valor

    def realizar_transacao(self, transacao):
        transacao.registrar_conta(self)


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500.0, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def pode_sacar(self, valor):
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques diários excedido.")
            return False
        if valor > self.limite:
            print("Valor excede o limite permitido.")
            return False
        if not super().pode_sacar(valor):
            print("Saldo insuficiente.")
            return False
        self.saques_realizados += 1
        return True


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


# Lista de clientes e contas
clientes = []
contas = []

# Menu interativo
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair
=> """


def encontrar_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None


def novo_usuario():
    cpf = input("CPF: ")
    if encontrar_cliente(cpf):
        print("Usuário já existe.")
        return
    nome = input("Nome: ")
    data_nascimento = input("Data nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)
    clientes.append(cliente)
    print("Usuário criado com sucesso.")


def nova_conta():
    cpf = input("CPF do usuário: ")
    cliente = encontrar_cliente(cpf)
    if not cliente:
        print("Usuário não encontrado.")
        return
    numero = len(contas) + 1
    conta = ContaCorrente(numero, cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print(f"Conta criada com sucesso: {conta.agencia}/{conta.numero}")


def listar_contas():
    for conta in contas:
        print(f"\nAgência: {conta.agencia}")
        print(f"Conta: {conta.numero}")
        print(f"Titular: {conta.cliente.nome}")


def depositar():
    cpf = input("CPF do usuário: ")
    cliente = encontrar_cliente(cpf)
    if not cliente or not cliente.contas:
        print("Cliente não encontrado ou sem conta.")
        return
    valor = float(input("Valor do depósito: "))
    transacao = Deposito(valor)
    cliente.contas[0].realizar_transacao(transacao)
    print("Depósito realizado.")


def sacar():
    cpf = input("CPF do usuário: ")
    cliente = encontrar_cliente(cpf)
    if not cliente or not cliente.contas:
        print("Cliente não encontrado ou sem conta.")
        return
    valor = float(input("Valor do saque: "))
    transacao = Saque(valor)
    if cliente.contas[0].realizar_transacao(transacao):
        print("Saque realizado.")


def extrato():
    cpf = input("CPF do usuário: ")
    cliente = encontrar_cliente(cpf)
    if not cliente or not cliente.contas:
        print("Cliente não encontrado ou sem conta.")
        return
    conta = cliente.contas[0]
    print("\n===== EXTRATO =====")
    for t in conta.historico.transacoes:
        print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
    print(f"Saldo atual: R$ {conta.saldo:.2f}")
    print("====================")


# Loop principal
while True:
    opcao = input(menu)

    if opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        extrato()
    elif opcao == "nu":
        novo_usuario()
    elif opcao == "nc":
        nova_conta()
    elif opcao == "lc":
        listar_contas()
    elif opcao == "q":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")