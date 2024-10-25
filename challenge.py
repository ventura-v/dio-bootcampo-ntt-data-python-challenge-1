balance = 0.0
daily_withdrawal_limit = 3
WITHDRAWAL_LIMIT = 500.00
operations = {}

print("Welcome to your bank account!\n")

while True:
  option = input("Please, choose which operation you want to do:\n D - Deposit\n W - Withdrawal\n S - Statement\n Q - Quit\n")

  if option.upper() == "D":
    amount = float(input("\nGreat! Please, enter the amount you wish to deposit:\n "))

    if amount > 0.0:
      operations.update({f"{len(operations) + 1} - deposit": f"R$ {amount:.2f}"})
      balance += amount

      print(f"Successful deposit!\n")
    else:
      print("Invalid amount! Please, enter a amount greater than 0.00\n")

  elif option.upper() == "W":
    amount = float(input("\nExcelent! Please, enter the amount you wish to withdraw:\n "))

    exceeds_balance = amount > balance
    exceeds_limite = amount > WITHDRAWAL_LIMIT

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

  elif option.upper() == "S":
    if not operations:
        print("\nNo transactions have been made")

    else:
      print("\nCompleted transactions:")

      for operation, amount in operations.items():
        print(operation, f" R$ {amount}")

    print(f"\nYour balance is: R$ {balance:.2f}\n")
    print(f"You have {daily_withdrawal_limit} daily withdrawals\n")

  elif option.upper() == "Q":
    print("\nSee you soon!")
    break

  else:
    print("\nInvalid option. Please, choose one of the available options.\n")
