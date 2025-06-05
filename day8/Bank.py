from abc import ABC , abstractmethod
class Account(ABC):
    @abstractmethod
    def get_balance(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class SavingsAccount(Account):
    __balance = 0

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        file = open("./newfile.txt","a")
        self.__balance += amount
        print("Deposited amount:", amount)
        file.write(f"Deposited amount is {amount}\n")
        file.close()

    def withdraw(self, amount):
        file = open("./newfile.txt","a")
        if self.__balance < amount:
            print("Not enough balance")
            return
        self.__balance -= amount
        print("Withdrawn amount", amount)
        file.write(f"withdrawn amount is {amount}\n")
        file.close()
class CurrentAccount(Account):

    __balance = 0
    withdrawlimit = 0

    def __init__(self,limit):
        self.withdrawlimit = limit

    def get_balance(self, amount):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        print("Deposited amount", amount)

    def withdraw(self, amount):
        if self.__balance + self.withdrawlimit < amount:
            print("Not enough balance")
            return
        self.__balance -= amount
        print("Withdrawn amount", amount)

class Bank:
    owner = "fun"
    accountnumber = 0
    def __init__(self, name, number, accounttype = "Savings", ):
        self.owner = name
        self.accountnumber = number
        if accounttype == "Savings":
            self.account = SavingsAccount()
        if accounttype == "Current":
            self.account = CurrentAccount(8000)
J = Bank("fun",1,"Savings")
J.account.deposit(100)
J.account.withdraw(50)