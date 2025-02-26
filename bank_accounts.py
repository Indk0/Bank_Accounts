# Display welcome message for the user
print('Welcome to the Earl of Mercia bank')

# Define the BankAccount class
class BankAccount:
    # Initialize the bank account with user details and balance
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        # Store user's personal information
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin

        # Convert balance from string format to float by removing currency 
        if isinstance(balance, str):
            self.balance = float(balance.replace('£', '').replace(',', ''))
        else:
            # Convert numeric balance to float
            self.balance = float(balance)
    
    # Display welcome message with user's name
    def display_wel_mes(self):
        print('----------------------')
        print(f"Welcome back {self.first_name} {self.last_name}.")
        print('----------------------')
    
    # Display current account balance
    def home(self):
        print(f'Your current account balance is: £{self.balance:,.2f}')
        print('----------------------')
    
    # Handle deposit and withdrawal transactions
    def payments_transfers(self, transactions, amount):
        if transactions.lower() == 'deposit':
            # Add the amount to the current balance
            self.balance += amount
            # Display confirmation message with the amount deposited
            print(f"Amount deposited: £{amount:,.2f}")
            print("Congrations on fending off the Vikings!!")
        elif transactions.lower() == 'withdraw':
            # Check if there are sufficient funds
            if self.balance >= amount:
                # Subtract the withdrawal amount from the balance
                self.balance -= amount
                # Display confirmation message with withdrew amount
                print(f"You withdrew: £{amount:,.2f}")
                print("Conquering more land? Good luck!")
            else:
                # Inform user of insufficient funds
                print("Insufficient balance.")
        else:
            # Handle invalid transaction type
            print('Invalid transaction type.')
        
    # Display new balance after transaction
    def display(self):
        print(f"Your new balance: £{self.balance:,.2f}")


# Create an instance of BankAccount with Leofric's information
Leofric = BankAccount('Leofric', 'Earl of Mercia', '96810571043', 'Current Account', '1040', '£3,097,576,293.76')

# Display welcome message for the user
Leofric.display_wel_mes()

# Main program loop
while True:
    # Display menu options
    print('----------------------')
    print('Please choose an option:')
    print('1. View current balance')
    print('2. Deposit money')
    print('3. Withdraw money')
    print('4. Exit')

    # Get user's choice
    choice = input('Enter your choice (1-4):')

    # Handle option 1: View balance
    if choice == '1':
        Leofric.home()
    
    # Handle option 2: Deposit money
    elif choice == '2':
        # Get deposit amount from user
        amount = float(input("Enter amount to deposit: "))
        # Process the deposit
        Leofric.payments_transfers('deposit',amount)
        # Display new balance
        Leofric.display()
    
    # Handle option 3: Withdraw money with PIN verification
    elif choice == '3':
        # Ask for PIN to verify identity
        security = input('Please enter your pin to withdraw:')
        # Verify the PIN
        if security == Leofric.pin:
            print('Your pin is correct.')
            # Get withdrawal amount
            amount = float(input("Enter amount to withdraw: "))
            # Process the withdrawal
            Leofric.payments_transfers('withdraw', amount)
            # Display new balance
            Leofric.display()
        else:
            # Handle incorrect PIN
            print('Incorrect PIN. Account locked please contact the bank.')
    
    # Handle option 4: Exit the program
    elif choice == "4":
        # Display goodbye message
        print("Goodbye! Have a prosperous rule, Leofric.")
        # Exit the loop to end the program
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice! Please select a valid option.")