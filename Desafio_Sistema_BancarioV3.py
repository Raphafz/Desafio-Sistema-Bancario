import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

banco = 'Bone Bank Corporation (BBC)'
slogan = 'Seu dinheiro em boas mãos'
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
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
            print ('\nOperação falhou! Você não tem saldo suficiente.')
        elif valor > 0:
            self._saldo -= valor
            print('\n----- Saque realizado com sucesso!-----')
            return True
        else:
         print('\nOperação falhou! O valor informado é inválido.')
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\n----- Valor depositado com sucesso!-----')
        else:
            print('\nOperação falhou! O valor informado é inválido.')
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao['tipo'] == Saque. __name__]
    )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print('\nOperação falhou! O valor do saque excede o limite.')
        elif excedeu_saques:
            print('\nOperação falhou! Número máximo de saques excedido.')
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        ) 
        
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
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
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu ():
    print('-'*41)
    print(f'{banco:^41}'.upper())
    print(f'{slogan:^41}')
    print('-'*41)
    menu = '''\n
             Seja bem-vindo ao BBC!
    ================ MENU ===================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova conta
    [6]\tListar contas
    [0]\tSair
    Selecione uma operação: '''
    return input(textwrap.dedent(menu)) 



def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return
    else:
        for conta in cliente.contas:
            print(f'{cliente.contas.index(conta)} - {conta.numero}')
        conta_desejada = int(input('Selecione a conta: '))
        return cliente.contas[conta_desejada]

def depositar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n====== Cliente não encontrado ========')
        return
    
    valor = float(input('Informe o valor do depósito: '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n====== Cliente não encontrado ========')
        return
    
    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n====== Cliente não encontrado ========')
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n---------------- EXTRATO ----------------")
    transacoes = conta.historico.transacoes
    
    extrato = ""
    if not transacoes:
        extrato = 'Não foram realizados movimentações.'
    else:
        for transacao in transacoes:
         extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
    
    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    print('------------------------------------------')

def criar_cliente(clientes):
    cpf = input('Informe o CPF (somente número): ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('\nJá existe um usuario com esse CPF!')
        return
    
    nome = input('Digite seu nome completo: ')
    data_nascimento = input('Digite sua data de nascimento (dd/mm/aa): ')
    endereco = input('Digite o seu endereço(logradouro, numero-bairro-cidade/sigla estado): ')

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print('\n---- Usuario criado com sucesso!----')

def criar_conta(numero_conta, clientes, contas):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n Cliente não encontrado, criação de conta encerrada!')
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print('='*100)
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
        elif opcao =='3':
            exibir_extrato(clientes)
        elif opcao == '4':
            criar_cliente(clientes)
        elif opcao == '5':
            numero_conta = len (contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao =='6':
            listar_contas(contas)
        elif opcao == '0':
            break
        else:
            print('\nOperação inválida, por favor selecione uma operação correta!')

main()
