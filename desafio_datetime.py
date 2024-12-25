from abc import ABC,abstractclassmethod, abstractproperty
import datetime 
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 10:
            print("\n Numero de transações excede o limite para hoje!!!")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, data_nascimento, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self):
        return f"<{self.__class__.__name__}: ({self.cpf})>"

class Conta:
     def __init__(self, numero, cliente):
         self._saldo = 0
         self._numero = numero
         self._agencia = "0001"
         self._cliente = cliente
         self._historico = Historico()

     @classmethod
     def nova_conta(cls, cliente, numero):
         return cls(numero, cliente)

     @property
     def saldo(self):
         return self._saldo
        
     @property
     def numero(self):
         return self._numero
     
     @property
     def agencia(self):
         return self._agencia
     
     @property
     def cliente(self):
         return self._cliente
     
     @property
     def historico(self):
         return self._historico  
     
     def sacar(self, valor):
         saldo = self.saldo
         excedeu_saldo = valor > saldo

         if excedeu_saldo:
             print("Saque não pode ser realizado! Saldo insuficiente!!")
         elif valor > 0:
             self._saldo -= valor
             print("\n Saque realizado com sucesso!!")
             return True
         else:
             print("\n Saque não realizado! Valor solicitado inválido!!")

         return False
     
     def depositar(self, valor):
         if valor > 0:
             self._saldo += valor
             print("Deposito realizado com sucesso!!")
         else:
             print("\n Depósito não realizado. Valor inválido!!")
             return False
         
         return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    # para a conta corrente o méthodo sacar da classe conta não segue
    # todas as diretrizes solicitadas, então vamos criar outro
    def sacar(self, valor):
        numero_saques = len (
            [transacao for transacao in self.historico.
             transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Valor do saque excede o limite! \nOperação não realizada!!!")
        elif excedeu_saques:
            print("Limite de saques excedidos. \nOperação não realizada!!!")
        else:
            return super().sacar(valor)
        
        return False

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"
    
    
    def __str__(self):
        return f"""
            Agencia:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
        return super().__str__()

class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self.transacoes
    
    def adionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.utcnow().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )
    
    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in None or transacao["tipo"].lower() == tipo_transacao.lower():
            yield transacao
        
    # def transacoes_do_dia(self):
    #     data_atual = datetime.utcnow().date()
    #     transacoes = []
    #     for transacao in self._transacoes:
    #         data_transacao = datetime.strptime(transacao["data"], 
    #                                            "%d-%m-%Y %H:%M:%S").date()
    #         if data_atual == data_transacao:
    #             transacoes.append(transacao)
    #     return transacoes

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self, conta):
        pass
    
class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    
class Deposito(Transacao): 
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open('log.txt', 'a') as arquivo:
            arquivo.write( 
                f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. Retornou {resultado}\n"
            )
        
        return resultado
    return envelope

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
 
def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não cadastrado")
        return
    
    return cliente.contas[0]

@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

@log_transacao  
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio(tipo_transacao="saque"):
        tem_transacao = True
        extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not transacao:
        extrato = "Não foram realizadas movimentações."

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))
     
def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == '1':
            depositar(clientes)

        elif opcao == '2':
            sacar(clientes)

        elif opcao == '3':
            exibir_extrato(clientes)

        elif opcao == '4':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao =='5':
            listar_contas(contas)
                    
        elif opcao == '6':
            criar_cliente(clientes)

        elif opcao == '0':
            break
        else:
            print('Operação Inválida, selecione novamente a operação')

main()