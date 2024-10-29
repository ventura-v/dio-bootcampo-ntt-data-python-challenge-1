def menu():
  choice = input("""
  Please, choose which operation you want to do:
  [D] - Deposit
  [W] - Withdrawal
  [S] - Statement
  [CU] - Create user
  [CA] - Create account
  [LA] - List accounts
  [Q] - Quit
  """)

  return choice

def deposit(balance, amount, operations, /):

  if amount > 0.0:
    operations.update({f"{len(operations) + 1} - deposit": f"R$ {amount:.2f}"})
    balance += amount
    print(f"Successful deposit!\n")
  else:
    print("Invalid amount! Please, enter a amount greater than 0.00\n")

  return balance

def withdrawlal(*, balance, amount, operations, withdrawal_limit, daily_withdrawal_limit):

    exceeds_balance = amount > balance
    exceeds_limite = amount > withdrawal_limit

    if exceeds_balance:
      print("amount greater than your balance account. Please, check your statement.\n")

    elif exceeds_limite: 
      print("amount greater than the R$ 500.00 limit per withdraw. Please, enter a amount up to 500.00\n")
      
    elif daily_withdrawal_limit <= 0:
      print("There's no more withdrawal limit today. Please, try again tomorrow.\n")
    
    elif amount > 0:
      operations.update({f"{len(operations) + 1} - withdraw": f"R$ {amount:.2f}"})
      balance -= amount
      daily_withdrawal_limit -= 1

      print(f"Successful withdrawal! You have {daily_withdrawal_limit} daily withdrawals\n")

    else:
      print("Invalid amount. Please, try a valid amount.\n")

    return balance, daily_withdrawal_limit

def statement(balance, /, *, operations, daily_withdrawal_limit):
  if not operations:
    print("\nNo transactions have been made")

  else:
    print("\nCompleted transactions:")

    for operation, amount in operations.items():
      print(operation, f" R$ {amount}")

    print(f"\nYour balance is: R$ {balance:.2f}\n")
    print(f"You have {daily_withdrawal_limit} daily withdrawals\n")

def new_user(name, birth, cpf, address, users):

  users.update({
      cpf: {
        "name": name,
        "birth": birth,
        "cpf": cpf,
        "address": address
      }
  })

def check_user(user_cpf, users):
  return user_cpf in users

def new_account(number, user_name, *, agency, accounts):
  accounts.update({
      f'{number}': {
          "agency": agency,
          "user": user_name
      }
  })

def list_accounts(accounts):
  for account, data_account in accounts.items():
    print(f"""
      Agency: {data_account['agency']}
      C/C: {account}
      Name: {data_account['user']}
    """)

def main():
  AGENCY = '0001'
  WITHDRAWAL_LIMIT = 500.00

  balance = 0.0
  daily_withdrawal_limit = 3
  operations = {}
  users = {}
  accounts = {}

  print("Welcome to our bank!\n")

  while True:
    option = menu()

    if option.upper() == "D":
      amount = float(input("\nGreat! Please, enter the amount you wish to deposit:\n "))

      balance = deposit(
        balance, 
        amount, 
        operations
      )

    elif option.upper() == "W":
      amount = float(input("\nExcelent! Please, enter the amount you wish to withdraw:\n "))

      balance, daily_withdrawal_limit = withdrawlal(
        balance=balance, 
        amount=amount, 
        operations=operations, 
        withdrawal_limit=WITHDRAWAL_LIMIT, 
        daily_withdrawal_limit=daily_withdrawal_limit
      )
    elif option.upper() == "S":
      statement(balance, operations=operations, daily_withdrawal_limit=daily_withdrawal_limit)

    elif option.upper() == "CU":
      print("\n Awesome! We need some informations:\n")
      cpf = input("\nEnter the CPF (only numbers):")
      user = check_user(cpf, users)

      if user:
        print("\nUser already in our system!")
      else:
        name = input("\nPlease, enter the name:")
        birth = input("\nNow, enter the date of birth (dd-mm-aaaa):")
        address_street = input("\nEnter the address street:")
        address_number = input("\nEnter the number:")
        address_neighborhood = input("\nEnter the neighborhood:")
        address_city_state = input("\nEnter the City and State (City/State):")
        address = f"{address_street}, {address_number} - {address_neighborhood} - {address_city_state}"

        new_user(name, birth, cpf, address, users)

    elif option.upper() == "CA":
      user_cpf = input("\nOK! We need to know which user will own the account. Please, enter the user CPF (only numbers): ")
      user = check_user(user_cpf, users)

      if not user:
        print("\nUser not found! Please, create the user first\n")
      else:
        number = len(accounts) + 1
        user_name = users[user_cpf].get('name')
        new_account(number, user_name, agency=AGENCY, accounts=accounts) 

    elif option.upper() == "LA":
      list_accounts(accounts)

    elif option.upper() == "Q":
      print("\nSee you soon!")
      break

    else:
      print("\nInvalid option. Please, choose one of the available options.\n")

main()