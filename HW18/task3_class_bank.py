class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number},\
 balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self._interest_rate = interest_rate

    def add_interest(self):
        self._balance += self._balance * self._interest_rate / 100


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def display_accounts(self):
        for account in self.accounts:
            print(account)

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif (
                isinstance(account, CurrentAccount) and
                account.get_balance() < 0
            ):
                print(f"Letter sent to account {account.get_account_number()}:\
 You are in overdraft.")

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account_number):
        self.accounts = [
            acc
            for acc in self.accounts
            if acc.get_account_number() != account_number
        ]

    def pay_dividend(self, amount):
        num_accounts = len(self.accounts)
        if num_accounts > 0:
            dividend_per_account = amount / num_accounts
            for account in self.accounts:
                account.deposit(dividend_per_account)


# Example usage
# Create an account with initial balance 1000
account1 = Account(1000, '1001')

# Create a savings account with initial balance 2000 and 5% interest rate
savings_account1 = SavingsAccount(2000, '2001', 5)

# Create a current account with initial balance 3000 and 1000 overdraft limit
current_account1 = CurrentAccount(3000, '3001', 1000)

# Create a bank
bank = Bank()

# Add accounts to the bank
bank.add_account(account1)
bank.add_account(savings_account1)
bank.add_account(current_account1)

# Update the accounts
bank.update()

# Display information about all accounts in the bank
print("Bank after opening a new account:")
bank.display_accounts()

# Create a new account with initial balance 500
new_account = Account(500, '4001')
bank.open_account(new_account)

# Display information about all accounts in the bank
print("Bank after opening a new account:")
bank.display_accounts()

# Close the account with account number '2001'
bank.close_account('2001')

# Display information about all accounts in the bank
print("Bank after closing account '2001':")
bank.display_accounts()

# Pay a dividend of 1200
bank.pay_dividend(1200)

# Display information about all accounts in the bank
print("Bank after paying dividend:")
bank.display_accounts()
