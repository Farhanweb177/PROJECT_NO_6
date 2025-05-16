class Bank:
    Bank_name = "state_bank"

    def __init__ (self, customer):
        self.customer = customer

    def show (self):
        print(f"customer: {self.customer}. Bank: {Bank.Bank_name}")

    @classmethod
    def change_name(cls, name):
        cls.Bank_name = name 

account_1 = Bank("farhan")
account_2 = Bank("ali")
account_3 = Bank("waqas")

account_1.show()
account_2.show()

Bank.change_name("karachi_bank")

account_1.show()
account_2.show()
