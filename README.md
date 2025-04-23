![deepseek_mermaid_20250423_f41abf](https://github.com/user-attachments/assets/c4cb891d-4c9f-43f5-ab51-48a7ec036308)# 🏦 Sistema Bancário POO - V3

![Bank System](https://img.icons8.com/color/48/000000/bank.png) *Sistema bancário orientado a objetos*

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Diagrama de Classes](#-diagrama-de-classes)
- [Funcionalidades](#-funcionalidades)
- [Como Executar](#-como-executar)
- [Próximas Atualizações](#-próximas-atualizações)
- [Conceitos POO Aplicados](#-conceitos-poo-aplicados)

## 🌐 Visão Geral

Sistema bancário completo implementado com **Programação Orientada a Objetos**, seguindo padrões de design e boas práticas de desenvolvimento.

```python
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

🛠️ Funcionalidades
Operações Bancárias
Operação	Descrição	Limites
Depósito	Valores positivos	-
Saque	Limite diário	R$ 500,00
Extrato	Histórico completo	Últimas 30 transações
Cadastros
👤 Clientes (PF)

💳 Contas Correntes

🔄 Transações

🚀 Como Executar
Clone o repositório:

bash
git clone https://github.com/seu-usuario/sistema-bancario-poo.git
Execute o sistema:

bash
python3 bancario_poo.py
Use o menu interativo:

======== MENU ========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar contas
[7] Sair
=> 
🔮 Próximas Atualizações
Implementação core POO

Persistência em banco de dados

Autenticação segura

Interface web

🧠 Conceitos POO Aplicados
Conceito	Aplicação
Abstração	Classe Transacao abstrata
Encapsulamento	Atributos privados (_saldo)
Herança	ContaCorrente herda de Conta
Polimorfismo	Método registrar()
Composição	Conta tem um Historico
Desenvolvido com ❤️ usando Python puro e padrões de projeto OO.


### Observações sobre o README.md:

1. **Formatação Markdown**:
   - Títulos com `#`
   - Códigos com ``` ```
   - Tabelas com `|`
   - Listas com `-` ou `[ ]`

2. **Elementos incluídos**:
   - Diagrama Mermaid (funciona no GitHub)
   - Tabela de funcionalidades
   - Roadmap de desenvolvimento
   - Exemplo de código
   - Índice navegável

3. **Personalização**:
   - Substitua os emojis se preferir
   - Adicione badges de status
   - Inclua seção de contribuição

4. **Renderização**:
   - Visualize o resultado no GitHub
   - Ou usando editores Markdown como VSCode
