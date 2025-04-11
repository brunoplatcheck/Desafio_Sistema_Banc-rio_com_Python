import re

MENU = """
    [1] Deposit
    [2] Withdraw
    [3] Statement
    [4] New User
    [5] New Account
    [6] List Accounts
    [7] Modify Account
    [8] Quit
=> """

AGENCY = "0001"
users = []
accounts = []

# Utility functions
def validate_cpf(cpf):
    cpf = re.sub(r"\D", "", cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
        check_digit = (value * 10 % 11) % 10
        if check_digit != int(cpf[i]):
            return False
    return True

def find_user(cpf):
    for user in users:
        if user["cpf"] == cpf:
            return user
    return None

def login():
    cpf = input("Enter your CPF: ")
    password = input("Enter your password: ")
    user = find_user(cpf)
    if user and user["password"] == password:
        return user
    print("Login failed: Invalid CPF or password.")
    return None

# Core functions
def deposit(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposit: $ {valor:.2f}\n"
        print("Deposit successful.")
    else:
        print("Invalid deposit amount.")
    return saldo, extrato

def withdraw(*, saldo, valor, extrato, limit, number_withdrawals, max_withdrawals):
    if valor <= 0:
        print("Invalid withdrawal amount.")
    elif valor > saldo:
        print("Insufficient balance.")
    elif valor > limit:
        print("Withdrawal limit exceeded ($500.00).")
    elif number_withdrawals >= max_withdrawals:
        print("Withdrawal limit reached for today.")
    else:
        saldo -= valor
        extrato += f"Withdraw: $ {valor:.2f}\n"
        number_withdrawals += 1
        print("Withdrawal successful.")
    return saldo, extrato, number_withdrawals

def show_statement(saldo, /, *, extrato):
    print("\n========== STATEMENT ===========")
    print("No transactions." if not extrato else extrato)
    print(f"\nCurrent balance: $ {saldo:.2f}")
    print("================================")

def create_user():
    cpf = re.sub(r"\D", "", input("Enter user's CPF: "))
    if not validate_cpf(cpf):
        print("Invalid CPF.")
        return
    if find_user(cpf):
        print("CPF already registered.")
        return

    name = input("Enter user's full name: ")
    birth_date = input("Enter birth date (dd/mm/yyyy): ")
    password = input("Set a password for the account: ")

    print("Enter address:")
    street = input("Street: ")
    number = input("Number: ")
    neighborhood = input("Neighborhood: ")
    city = input("City: ")
    state = input("State (abbreviation): ")

    address = f"{street}, {number} - {neighborhood} - {city}/{state}"
    users.append({"name": name, "birth_date": birth_date, "cpf": cpf, "address": address, "password": password})
    print("User created successfully.")

def create_account():
    cpf = input("Enter the CPF of the user: ")
    user = find_user(cpf)
    if user:
        number = len(accounts) + 1
        accounts.append({"agency": AGENCY, "number": number, "user": user})
        print("Account created successfully.")
    else:
        print("User not found. Account not created.")

def list_accounts():
    for account in accounts:
        print(f"Agency: {account['agency']} | Account Number: {account['number']} | Holder: {account['user']['name']}")

def modify_account():
    user = login()
    if not user:
        return

    new_name = input(f"Enter new name (or leave blank to keep '{user['name']}'): ")
    if new_name:
        user["name"] = new_name
    new_password = input("Enter new password (or leave blank to keep current): ")
    if new_password:
        user["password"] = new_password
    print("Account updated successfully.")

# Main loop
saldo = 0
limit = 500
extrato = ""
number_withdrawals = 0
MAX_WITHDRAWALS = 3

while True:
    option = input(MENU)

    if option == "1":
        if login():
            value = float(input("Enter deposit amount: $ "))
            saldo, extrato = deposit(saldo, value, extrato)

    elif option == "2":
        if login():
            value = float(input("Enter withdrawal amount: $ "))
            saldo, extrato, number_withdrawals = withdraw(
                saldo=saldo, valor=value, extrato=extrato,
                limit=limit, number_withdrawals=number_withdrawals, max_withdrawals=MAX_WITHDRAWALS
            )

    elif option == "3":
        if login():
            show_statement(saldo, extrato=extrato)

    elif option == "4":
        create_user()

    elif option == "5":
        create_account()

    elif option == "6":
        list_accounts()

    elif option == "7":
        modify_account()

    elif option == "8":
        print("Exiting system. Thank you!")
        break

    else:
        print("Invalid option, please choose again.")
