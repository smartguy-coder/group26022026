


class Person:
    def __init__(self, name: str):
        self.name = name.strip().title()
        print('created ', self)

    def __str__(self):
        return f"Person {self.name}"


class BankAccount:
    def __init__(self, owner: Person, bank: "Bank"):
        self.balance = 0
        self.owner = owner
        self.bank = bank
        print(self)

    def __str__(self):
        return f"Account was opened in {self.bank} for {self.owner.name}"


class Bank:
    def __init__(self, title: str):
        self.title = f'LTD {title.strip().upper()}'
        print(self)

    def open_account(self, client: Person) -> BankAccount:
        bank_account = BankAccount(owner=client, bank=self)

        return bank_account

    def __str__(self):
        return f"{self.title}"