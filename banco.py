print('Bem vindo ao Banco do Povo. \n\t Menu de opções:\n')

#opt = input()

saldo = 0
limite = 500
extrato = ""
n_saques = 0
l_saques = 3

while True:

    opt = input('\t [1] --> depósito\n\t [2] --> saque\n\t [3] --> extrato\n\t [0] --> sair \n')
    
    if opt == '1':
        valor = float(input('Depósito --> informa o valor: '))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.f}\n"
        else:
            print("Impossível depositar valor negativo!")

    elif opt == '2':
        valor = float(input('Saque --> informa o valor: '))
        if valor > saldo:
            print("Saldo Insuficiente saque não realizado")
        elif valor > limite:
            print("Limite excedido, saque não realizado")
        elif n_saques > l_saques:
            print("Número de saques excede 3, saque não realizado")
        elif valor > 0:
            saldo -+ valor
            extrato += f"Saque: R${valor:.2f}\n"
            n_saques += 1
        else:
            print("Saque não realizado, valor inválido")    
    
    elif opt == '3':
        print("\tExtrato: ")
        if not extrato:
            print("Sem movimentações")
        else:
            print(extrato)
            print(f"Saldo: R${saldo:.2f}\n")

    elif opt == '0':
        break
    else:
        print('Operação Inválida, selecione novamente a operação')


