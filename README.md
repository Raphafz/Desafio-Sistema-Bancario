# Desafio

## Sobre
Esse é um dos desafios de código propostos no Bootcamp DIO, Python AI Backend Developer.


O tema é "Criando um Sistema Bancário com Python". Onde a intenção do código é implementar três operações: depósito, saque e extrato para um banco que deseja monetizar suas operações em Python.

## Tecnologias
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Versão 1

### Operação de depósito
Deve ser possível depositar valores positivos para uma conta bancária. A v1 do projeto trabalha com apenas 1 usuário, então não é necessário se preocupar com a identificação do número da agência e nem da conta bancária.

Todos os depósitos devem ser armazenados numa variável e exibidos na operação de extrato.

### Operação de saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00/saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar dinheiro por falta de saldo.

Todos os saques devem ser armazenados numa variável e exibidos na operação de extrato.

### Operação de extrato
Deve listar todos os depósitos e saques realizados na conta. No fim da lista, deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx.

## Versão 2
O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo.
Vamos criar funçoes para as operações extrato, sacar, deposito e visualizar histórico. Além disso, para a versão 2 do nosso sistema vamos criar duas novas funções: criar usuário (cliente do banco) e cria conta corrente (vincular com usuário).

## Versão 3
iremos atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML.