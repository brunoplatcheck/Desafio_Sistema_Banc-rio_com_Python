from abc import ABC, abstractmethod
from datetime import date
import re

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Historico:
    def __init__(self):
        self._transacoes = []
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

    @property
    def transacoes(self):
        return self._transacoes

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(f"Depósito: R$ {self.valor:.2f}")

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(f"Saque: R$ {self.valor:.2f}")

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
        if valor <= 0:
            print("Valor inválido para saque.")
            return False
        
        if self._saldo < valor:
            print("Saldo insuficiente.")
            return False
        
        self._saldo -= valor
        return True
    
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False
        
        self._saldo += valor
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    def sacar(self, valor):
        if valor > self._limite:
            print(f"Valor excede o limite de R$ {self._limite:.2f} por saque.")
            return False
        
        return super().sacar(valor)

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento

def menu():
    print("\n======== MENU ========")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Novo usuário")
    print("[5] Nova conta")
    print("[6] Listar contas")
    print("[7] Sair")
    return input("=> ")

def validar_cpf(cpf):
    cpf = re.sub(r"\D", "", cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
        check_digit = (value * 10 % 11) % 10
        if check_digit != int(cpf[i]):
            return False
    return True

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            numero_conta = int(input("Número da conta: "))
            valor = float(input("Valor do depósito: R$ "))
            
            conta = next((c for c in contas if c.numero == numero_conta), None)
            if conta:
                transacao = Deposito(valor)
                conta.cliente.realizar_transacao(conta, transacao)
            else:
                print("Conta não encontrada.")

        elif opcao == "2":
            numero_conta = int(input("Número da conta: "))
            valor = float(input("Valor do saque: R$ "))
            
            conta = next((c for c in contas if c.numero == numero_conta), None)
            if conta:
                transacao = Saque(valor)
                conta.cliente.realizar_transacao(conta, transacao)
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            numero_conta = int(input("Número da conta: "))
            conta = next((c for c in contas if c.numero == numero_conta), None)
            
            if conta:
                print("\n======== EXTRATO ========")
                if not conta.historico.transacoes:
                    print("Não foram realizadas movimentações.")
                else:
                    for transacao in conta.historico.transacoes:
                        print(transacao)
                print(f"\nSaldo: R$ {conta.saldo:.2f}")
                print("========================")
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            cpf = input("CPF (somente números): ")
            if not validar_cpf(cpf):
                print("CPF inválido.")
                continue
            
            if any(cliente.cpf == cpf for cliente in clientes):
                print("CPF já cadastrado.")
                continue
            
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            
            cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
            clientes.append(cliente)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "5":
            cpf = input("CPF do usuário: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            
            if cliente:
                numero = len(contas) + 1
                conta = ContaCorrente.nova_conta(cliente, numero)
                cliente.adicionar_conta(conta)
                contas.append(conta)
                print(f"Conta criada com sucesso! Número: {numero}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "6":
            for conta in contas:
                print(f"Agência: {conta.agencia} | Número: {conta.numero} | Titular: {conta.cliente.nome}")

        elif opcao == "7":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, por favor selecione novamente.")

if __name__ == "__main__":
    main()