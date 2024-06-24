class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance, password):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.password = password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance is {self.balance}.")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance, password):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, account_holder, initial_balance, password)
            print(f"Account created for {account_holder} with account number {account_number}.")

    def login(self, account_number, password):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if account.password == password:
                print(f"Welcome {account.account_holder}!")
                return account
            else:
                print("Incorrect password.")
        else:
            print("Account not found.")
        return None

def main():
    bank = Bank()
    while True:
        print("\nWelcome to the Banking System")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            password = input("Enter password: ")
            bank.create_account(account_number, account_holder, initial_balance, password)
        elif choice == '2':
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            account = bank.login(account_number, password)
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == '1':
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif sub_choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif sub_choice == '3':
                        account.check_balance()
                    elif sub_choice == '4':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()