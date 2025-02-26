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
            self.balance += deposit()



Leofric = BankAccount('Leofric', 'Earl of Mercia', '96810571043', 'Current Account', '1040', '£3,097,576,293')

