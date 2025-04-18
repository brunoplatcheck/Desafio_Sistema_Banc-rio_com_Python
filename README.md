# 🏦 Bank System V2

Este é um projeto de simulação de sistema bancário desenvolvido em Python. Ele permite a criação de usuários, contas bancárias e a realização de operações como depósitos, saques e visualização de extratos, com autenticação via CPF e senha.

## 📋 Funcionalidades

- [1] **Depósito**  
- [2] **Saque**  
- [3] **Extrato**  
- [4] **Novo Usuário**  
- [5] **Nova Conta**  
- [6] **Listar Contas**  
- [7] **Modificar Conta**  
- [8] **Sair**

> As operações 1, 2, 3 e 7 exigem **login via CPF e senha**.

## 🔒 Segurança

- Verificação de **CPF válido** com base nos dígitos verificadores.
- **Senha** obrigatória para cada usuário.
- Login requerido para ações sensíveis.

## 📌 Cadastro de Usuário

- CPF (com validação)
- Nome completo
- Data de nascimento
- Senha de acesso
- Endereço (informado separadamente e concatenado)

## 📌 Cadastro de Conta

- Associada a um usuário já existente (via CPF)
- Agência padrão: `0001`
- Número da conta gerado automaticamente

## 🧾 Regras do Sistema

- **Limite de saque:** R$ 500,00 por operação
- **Máximo de saques diários:** 3
- **Depósitos e saques:** Valores precisam ser positivos
- **Extrato:** Armazena histórico de movimentações

## ▶️ Como usar

1. Execute o programa em um terminal com Python 3:
   ```bash
   python nome_do_arquivo.py
   ```

2. Escolha uma das opções do menu.

3. Para utilizar funcionalidades de conta, certifique-se de:
   - Criar um usuário [4]
   - Criar uma conta associada [5]

## 💡 Melhorias Futuras

- Armazenamento em arquivos ou banco de dados
- Interface gráfica com Tkinter ou web com Flask
- Registro de tempo nas transações
- Diferentes tipos de contas (corrente, poupança)
