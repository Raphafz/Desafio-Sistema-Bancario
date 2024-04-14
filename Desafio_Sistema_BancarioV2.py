import textwrap

banco = 'Bone Bank Corporation (BBC)'
slogan = 'Seu dinheiro em boas mãos'

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




def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print('\n----- Valor depositado com sucesso!-----')

    else:
            print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
      print("\nOperação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print('\n----- Saque realizado com sucesso!-----')
        

    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo,/, *, extrato ):
    print("\n---------------- EXTRATO ----------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.2f}")
    print("------------------------------------------")

def criar_usuario(usuarios):
    cpf= input('Digite o seu CPF (somente números): ')
    usuario= filtrar_usuarios(cpf, usuarios)
    if usuario:
        print('\nJá existe um usuario com esse CPF!')
        return
    nome = input('Digite seu nome completo: ')
    data_nascimento = input('Digite sua data de nascimento (dd/mm/aa): ')
    endereco = input('Digite o seu endereço(logradouro, numero-bairro-cidade/sigla estado): ')
    usuarios.append({"nome": nome, "data_nascimeto": data_nascimento, "cpf": cpf, "endereco": endereco})
    print('\n---- Usuario criado com sucesso!----')

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, criação de conta encerrada!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
    
        opcao = menu()
        
        if opcao == '1':
            valor = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
        elif opcao =='3':
            exibir_extrato(saldo, extrato = extrato)
        elif opcao == '4':
            criar_usuario(usuarios)
        elif opcao == '5':
            numero_conta = len (contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao =='6':
            listar_contas(contas)
        elif opcao == '0':
            break
        else:
            print('\nOperação inválida, por favor selecione uma operação correta!')

main()