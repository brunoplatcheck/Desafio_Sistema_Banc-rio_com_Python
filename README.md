# 🏦 Sistema Bancário em Python

Este é um projeto de um sistema bancário simples desenvolvido em Python, com suporte às operações básicas de **depósito**, **saque** e **extrato**. Ele simula o funcionamento de uma conta bancária, sendo ideal para fins didáticos e de aprendizado da linguagem.

## 📋 Funcionalidades

- 💰 **Depósito**: Permite adicionar valores positivos à conta.

- 🏧 **Saque**:
  - Limite de **3 saques diários**.
  - Valor máximo por saque: **R$ 500,00**.
  - Saques só são permitidos se houver saldo suficiente.

- 📄 **Extrato**:
  - Lista todos os depósitos e saques realizados.
  - Exibe o **saldo atual da conta**.
  - Formata os valores no padrão `R$ xxx.xx`.

## 🧠 Lógica utilizada

- Armazena o **saldo**, o **histórico de transações** e a **quantidade de saques** com variáveis simples.
- Utiliza **condições e laços** para controlar o menu e validar as regras.
- Simples e funcional, sem necessidade de conexão com banco de dados.

## 🚀 Como executar

1. Certifique-se de ter o Python instalado na sua máquina.
2. Clone ou baixe este repositório.
3. Execute o arquivo `banco.py` (ou o nome que você salvou o projeto) no terminal:

```bash
python banco.py
💡 Exemplo de uso
text
Copiar
Editar
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 1000
Depósito realizado com sucesso.

=> s
Informe o valor do saque: 300
Saque realizado com sucesso.

=> e
========== EXTRATO ==========
Depósito: R$ 1000.00
Saque:    R$ 300.00

Saldo atual: R$ 700.00
=============================
👨‍💻 Desenvolvedor
Feito por brunoplatcheck

🍴 Fork do projeto
Você pode acessar ou fazer fork deste projeto diretamente pelo GitHub:
👉 https://github.com/brunoplatcheck/Desafio_Sistema_Banc-rio_com_Python

📄 Licença
Este projeto é livre para uso educacional.

go
Copiar
Editar

Se quiser, posso te gerar o arquivo `.md` para baixar direto também!
