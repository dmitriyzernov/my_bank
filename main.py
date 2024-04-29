class Customer:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, first_name, last_name, passport_number):
        customer = Customer(first_name, last_name, passport_number)
        self.customers[customer.passport_number] = customer

    def add_account(self, account, customer):
        self.accounts[customer] = account

    def deposit(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.deposit(amount)

    def withdraw(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.withdraw(amount)

    def get_customer(self, passport_number):
        if passport_number not in self.customers:
            raise KeyError("Customer not found")
        return self.customers[passport_number]

    def get_customer_account(self, passport_number):
        customer = self.get_customer(passport_number)
        if customer not in self.accounts:
            raise KeyError("Account not found")
        return self.accounts[customer]


class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.amount = 0
        self.currency = currency

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if amount > self.amount:
            raise ValueError("Недостаточно денег на счету")
        self.amount -= amount



if __name__ == '__main__':
    bank = Bank()
    bank.add_customer('Tony', 'Stark', 77801319)
    customer_1 = bank.get_customer(77801319)

    bank.add_customer('Sonik', 'Alkony', 88223311)
    customer_2 = bank.get_customer(88223311)

    my_bank_1 = BankAccount(1120222, "USD")
    my_bank_2 = BankAccount(2233444, "USD")

    bank.add_account(my_bank_1, customer_1)
    bank.add_account(my_bank_2, customer_2)

    my_bank_1.deposit(100)
    my_bank_2.deposit(100)



