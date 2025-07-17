from datetime import datetime

# Constantes
LIMITE_SAQUES = 3
AGENCIA = "0001"

# Variáveis globais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("O valor excede o limite permitido.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"{datetime.now()} - Saque: R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")
    else:
        print("Valor inválido.")
    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"{datetime.now()} - Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO =====")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===================")


def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário já cadastrado.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")


def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)

    if usuario:
        numero_conta = len(contas) + 1
        contas.append({
            "agencia": AGENCIA,
            "numero_conta": numero_conta,
            "usuario": usuario
        })
        print(f"Conta criada com sucesso! Agência: {AGENCIA} Conta: {numero_conta}")
    else:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")


def listar_contas():
    for conta in contas:
        print(f"\nAgência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair
=> """

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == 's':
        valor = float(input("Valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == 'e':
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'nu':
        criar_usuario()

    elif opcao == 'nc':
        criar_conta()

    elif opcao == 'lc':
        listar_contas()

    elif opcao == 'q':
        print("Saindo do sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida.")