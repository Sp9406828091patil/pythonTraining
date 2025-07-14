import random
class BankAccount:
    def __init__(self):
        self.accountDetailsDirectory = {}
       
    def createAccount(self, newAccountNumber, name, age, gender, initialBalance = 0):
        if len(self.accountDetailsDirectory) == 0:

            # create new dict
            personDetails = {
                'name' : name,
                'age' : age,
                'gender' : gender,
                'initialBalance' : initialBalance
            }
 
            # Add account details in accountDeatilsDirectory
            self.accountDetailsDirectory[newAccountNumber] = personDetails
            print('Account create successfully')     
        else:
            allAccountNumbers = list(self.accountDetailsDirectory.keys())
            if newAccountNumber in allAccountNumbers:
                raise ValueError('Account number already exists')
            else:
                # create new dict
                personDetails = {
                    'name' : name,
                    'age' : age,
                    'gender' : gender,
                    'initialBalance' : initialBalance
                    }
 
                # Add account details in accountDeatilsDirectory
                self.accountDetailsDirectory[newAccountNumber] = personDetails
                print('Account create successfully')

 
account = BankAccount()
account.createAccount(251110, 'Aboli', 25, 'Female', 10000000)
account.createAccount(12345, 'Sagar', 35, 'Male', 200)
account.createAccount(251110, 'Abolis', 255, 'Females', 1000)     
 
                                         
       
 
    # def deposit(self, amount):
    #     self.balance += amount
    #     return self.balance
       
    # def withdraw(self, amount):
    #     if amount > self.balance:
    #         raise ValueError('Indequate Balance')
    #     else:
    #         self.balance -= amount
    #     return self.balance