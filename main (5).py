class BankAccount:
    def __init__(self, account_number: str, account_holder_name: str, account_balance: float):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance

    def deposit(self, amount: float) -> None:
        self.__account_balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.__account_balance:
            print("Insufficient balance")
        else:
            self.__account_balance -= amount

    def display_balance(self) -> float:
        return self.__account_balance


# Test the BankAccount class
bank_account = BankAccount("123456789", "John Doe", 1000.0)
print(f"Initial balance: {bank_account.display_balance()}")

bank_account.deposit(500.0)
print(f"Balance after deposit: {bank_account.display_balance()}")

bank_account.withdraw(200.0)
print(f"Balance after withdrawal: {bank_account.display_balance()}")

bank_account.withdraw(1500.0)
print(f"Balance after withdrawal: {bank_account.display_balance()}")
