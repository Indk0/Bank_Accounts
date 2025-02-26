print('Welcome to the Earl of Mercia bank')

class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
    
    def display_wel_mes(self):
        print('----------------------')
        print(f"Welcome back {self.first_name} {self.last_name}.")
        print('----------------------')
    
    def home(self):
        print(f'Your current account balance is: {self.balance}')
    
    def payments_transfers(self):
        if BankAccount.deposit():
            deposit = input(float("Enter amount to be deposited:"))
            self.balance += deposit
            print("Amount deposited:", deposit)
            print("Congrations on defending againts the Vikings!!")
        
        elif BankAccount.withdraw(self):
            withdraw = input(float("Enter amount to be withdrawn:"))
            if self.balance >= withdraw:
                self.balance -= withdraw
                print("You withdrew:", withdraw)
                print("Conquering more land? Good luck!")
            else:
                print("Insufficient balance.")

        def display(self):
            print(f"Your remaining balance:", self.balance)



Leofric = BankAccount('Leofric', 'Earl of Mercia', '96810571043', 'Current Account', '1040', '£3,097,576,293')

Leofric.display_wel_mes
Leofric.home
