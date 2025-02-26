print('Welcome to the Earl of Mercia bank')

class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin

        # Convert balance from string format to float by removing currency symbol and commas
        if isinstance(balance, str):
            self.balance = float(balance.replace('£', '').replace(',', ''))
        else:
            self.balance = float(balance)
    
    def display_wel_mes(self):
        print('----------------------')
        print(f"Welcome back {self.first_name} {self.last_name}.")
        print('----------------------')
    
    def home(self):
        print(f'Your current account balance is: £{self.balance:,.2f}')
        print('----------------------')
    
    def payments_transfers(self, transactions, amount):
        if transactions.lower() == 'deposit':
            self.balance += amount
            print(f"Amount deposited: £{amount:,.2f}")
            print("Congrations on fending off the Vikings!!")
        elif transactions.lower() == 'withdraw':
            if self.balance >= amount:
                self.balance -= amount
                print(f"You withdrew: £{amount:,.2f}")
                print("Conquering more land? Good luck!")
            else:
                print("Insufficient balance.")
        else:
            print('Invalid transaction type.')
    
    def display(self):
        print(f"Your remaining balance: £{self.balance:,.2f}")


# Initialize with the same value but it will be converted to a number
Leofric = BankAccount('Leofric', 'Earl of Mercia', '96810571043', 'Current Account', '1040', '£3,097,576,293.76')

Leofric.display_wel_mes()

while True:
    print('----------------------')
    print('Please choose an option:')
    print('1. View current balance')
    print('2. Deposit money')
    print('3. Withdraw money')
    print('4. Exit')

    choice = input('Enter your choice (1-4):')

    if choice == '1':
        Leofric.home()
    
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        Leofric.payments_transfers('deposit',amount)
    
    elif choice == '3':
        security = input('Please enter your pin to withdraw:')
        if security == Leofric.pin:
            print('Your pin is correct.')
            amount = float(input("Enter amount to withdraw: "))
            Leofric.payments_transfers('withdraw', amount)
        else:
            print('Incorrect PIN. Account locked please contact the bank.')
    
    elif choice == "4":
        print("Goodbye! Have a prosperous rule, Leofric.")
        break

    else:
        print("Invalid choice! Please select a valid option.")