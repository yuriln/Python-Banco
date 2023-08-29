menu = """
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

"""

saldo = 300
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
limite_diario = 1500

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(extrato)
    else:
        print("Valor informado inválido")

def sacar(valor):
    global saldo, extrato, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou, você não tem saldo suficiente.")
    elif excedeu_saques:
        print("Você atingiu o limite de saques diários, tente amanhã.")
    elif excedeu_limite:
        print("Valor excedeu o limite da conta.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(extrato)
    else:
        print("Operação falhou, valor inválido.")

def exibir_extrato():
    global extrato, saldo
    print("\n===============EXTRATO================")
    if not extrato:
        print("Não foram realizadas movimentações")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==============================")

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao == "2":
        valor = float(input("Qual o valor a ser sacado: "))
        sacar(valor)

    elif opcao == "3":
        exibir_extrato()

    elif opcao == "4":
        print("Saindo")
        break

    else:
        print("Opção inválida, tente novamente")