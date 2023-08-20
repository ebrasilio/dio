import textwrap

def menu():
    menu = """\n
    ................... Opções ..................
    [1] --> Deposito
    [2] --> Retirada
    [3] --> Extrato
    [4] --> Nova Conta
    [5] --> Listar Contas
    [6] --> Novo Usuário
    [0] --> Sair
    -->  """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
         saldo += valor
         extrato += f"Depósito:\tR$ {valor:.2f}\n"
    else:
         print("Impossível depositar valor negativo!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo Insuficiente saque não realizado")
    elif valor > limite:
       print("Limite excedido, saque não realizado")
    elif numero_saques > limite_saques:
        print("Número de saques excede 3, saque não realizado")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Saque não realizado, valor inválido")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(".................................................")
    print(".....................Extrato.....................\n")
    if not extrato:
        print("Sem movimentações")
    else:
        print(extrato)
        print(f"--> Saldo:\tR${saldo:.2f}\n")
        print(".................................................")

def criar_usuario(usuarios):
    cpf = input("Inform o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, no. - bairro - cidade/sigla Estado: )")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, 
                     "cpf": cpf, "endereco": endereco })
    print("\nUsuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso !")
        return {"agencia": agencia, "numero_conta": numero_conta,"usuario": usuario}

    print("Usuário não encontrado, conta não criada") 

def listar_conta(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" *100)
        print(textwrap.dedent(linha))
        
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        opt = menu()

        if opt == '1':
            valor = float(input('Depósito --> informe o valor: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opt == '2':
            valor = float(input('Saque --> informa o valor: '))
            saldo, extrato = sacar(saldo=saldo,
                                   valor=valor,
                                   extrato=extrato,
                                   limite=limite,
                                   numero_saques=numero_saques,
                                   limite_saques=LIMITE_SAQUES
            )
    
        elif opt == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opt == '4':
            numero_conta = len(contas) + 1 
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta) 

        elif opt == '5':
            listar_conta(contas)
                     
        elif opt == '6':
            criar_usuario(usuarios)
        elif opt == '0':
            break
        else:
            print('Operação Inválida, selecione novamente a operação')

main()
=======
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