import textwrap

def menu():
    menu = """ \n
    ................... Operacoes .................
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Conta
    [nu]\tNovo Usuario
    [q]\tSair
    --> """
    return input(textwrap.dedent(menu))    

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Impossível depositar valor negativo!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques,limite_saques):
    if valor > saldo:
        print("Saldo Insuficiente saque não realizado")
    elif valor > limite:
        print("Limite excedido, saque não realizado")
    elif numero_saques > limite_saques:
        print("Número de saques excede 3, saque não realizado")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:/tR$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Saque não realizado, valor inválido")    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(".................. EXTRATO ................")
    if not extrato:
        print("Sem movimentações")
    else:
        print(extrato)
        print(f"--> Saldo:\tR${saldo:.2f}\n")
        print("...........................................")


def criar_usuario(usuarios):
    return

def criar_conta(agencia, numero_conta, usuarios):
    return

def listar_contas(contas):
    return

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Depósito --> informe o valor: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Saque --> informe o valor: '))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
                
        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1

        elif opcao == 'q':
            break
        else:
            print('Operação Inválida, selecione novamente a operação')
        

main()    