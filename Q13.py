# BANK ACCOUNT MANAGEMENT SYSTEM

accounts = []          # accounts will store there
next_account_number = 1001   # number will assign automatically while creating account.


# function to create a new account..

def create_account(name, initial_deposit):
    global next_account_number

    new_account = {
        "account_number": next_account_number,
        "name": name,
        "balance": initial_deposit,
        "history": []   # yaha saari transactions record hongi
    }

    new_account["history"].append(f"Account opened with balance {initial_deposit}")
    accounts.append(new_account)

    print(f"Account created successfully! Account Number: {next_account_number}, Name: {name}")
    next_account_number += 1


# helper function to find account by account number..

def find_account(account_number):
    for acc in accounts:
        if acc["account_number"] == account_number:
            return acc
    return None


# function to deposit money..

def deposit(account_number, amount):
    acc = find_account(account_number)

    if acc is None:
        print("Account not found.")
        return

    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return

    acc["balance"] += amount
    acc["history"].append(f"Deposited {amount}")
    print(f"Deposited {amount} into account {account_number}. New balance: {acc['balance']}")


# function to withdraw money..

def withdraw(account_number, amount):
    acc = find_account(account_number)

    if acc is None:
        print("Account not found.")
        return

    if amount <= 0:
        print("Withdraw amount must be greater than zero.")
        return

    if amount > acc["balance"]:
        print("Insufficient balance.")
        return

    acc["balance"] -= amount
    acc["history"].append(f"Withdrew {amount}")
    print(f"Withdrew {amount} from account {account_number}. New balance: {acc['balance']}")



# function to transfer money between two accounts..

def transfer(from_account_number, to_account_number, amount):
    from_acc = find_account(from_account_number)
    to_acc = find_account(to_account_number)

    if from_acc is None or to_acc is None:
        print("One or both accounts not found.")
        return

    if amount <= 0:
        print("Transfer amount must be greater than zero.")
        return

    if amount > from_acc["balance"]:
        print("Insufficient balance for transfer.")
        return

    from_acc["balance"] -= amount
    to_acc["balance"] += amount

    from_acc["history"].append(f"Transferred {amount} to account {to_account_number}")
    to_acc["history"].append(f"Received {amount} from account {from_account_number}")

    print(f"Transferred {amount} from account {from_account_number} to account {to_account_number}")



# function to check balance..

def check_balance(account_number):
    acc = find_account(account_number)

    if acc is None:
        print("Account not found.")
        return

    print(f"Account {account_number} ({acc['name']}) balance: {acc['balance']}")



# function to show transaction history..

def show_history(account_number):
    acc = find_account(account_number)

    if acc is None:
        print("Account not found.")
        return

    print(f"\n----- Transaction History for Account {account_number} ({acc['name']}) -----")
    if len(acc["history"]) == 0:
        print("No transactions yet.")
        return

    for record in acc["history"]:
        print(f"- {record}")


# function to apply yearly interest (5%)..

def apply_interest(account_number):
    acc = find_account(account_number)

    if acc is None:
        print("Account not found.")
        return

    interest_rate = 0.05
    interest_amount = acc["balance"] * interest_rate
    acc["balance"] += interest_amount
    acc["history"].append(f"Interest added: {interest_amount:.2f}")

    print(f"Interest of {interest_amount:.2f} added to account {account_number}. New balance: {acc['balance']:.2f}")


# function to delete an account..

def delete_account(account_number):
    acc = find_account(account_number)

    if acc is None:
        print("Account not found.")
        return

    accounts.remove(acc)
    print(f"Account {account_number} deleted successfully.")


# function to show all accounts..

def show_all_accounts():
    print("\n----- ALL ACCOUNTS -----")
    if len(accounts) == 0:
        print("No accounts yet.")
        return

    for acc in accounts:
        print(f"Account {acc['account_number']}: {acc['name']} -> Balance: {acc['balance']}")


# function to display the menu..

def show_menu():
    print("\n===== BANK MENU =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Show Transaction History")
    print("7. Apply Interest")
    print("8. Delete Account")
    print("9. Show All Accounts")
    print("10. Exit")


# MAIN PROGRAM - menu-driven loop..

if __name__ == "__main__":

    while True:
        show_menu()
        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            name = input("Enter account holder name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            create_account(name, initial_deposit)

        elif choice == "2":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            deposit(acc_num, amount)

        elif choice == "3":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter withdraw amount: "))
            withdraw(acc_num, amount)

        elif choice == "4":
            from_acc = int(input("Enter your account number: "))
            to_acc = int(input("Enter recipient account number: "))
            amount = float(input("Enter transfer amount: "))
            transfer(from_acc, to_acc, amount)

        elif choice == "5":
            acc_num = int(input("Enter account number: "))
            check_balance(acc_num)

        elif choice == "6":
            acc_num = int(input("Enter account number: "))
            show_history(acc_num)

        elif choice == "7":
            acc_num = int(input("Enter account number: "))
            apply_interest(acc_num)

        elif choice == "8":
            acc_num = int(input("Enter account number: "))
            delete_account(acc_num)

        elif choice == "9":
            show_all_accounts()

        elif choice == "10":
            print("Thank you for using the Bank System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 10.")