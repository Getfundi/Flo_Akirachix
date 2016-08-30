from datetime import datetime

class MPESA(object):
    """docstring for MPESA
"""
    def __init__(self):
        self.name=input("Please enter the account name\n")
        self.number=input("Please enter the phone number\n")
        self.balance=0.0
        self.deposits=[]
        self.withdrawals=[]
        print("welcome",self.name)
    def deposit(self,amount):
        # self.balance+=amount
        # print("Dear",self.name,"your","have","deposited",self.deposit,"your","balance","is",self.balance,"is")
        if amount<50:
            print("you cannot deposit less")
        else:
            self.balance+=amount
            # self.deposits.append(amount)
            now=datetime.now()
            time=now.strftime("%c")
            details={"time":time,"amount":amount}
            self.deposits.append(details)
            print("Dear",self.name,"you have deposited this amount",amount,"your current balance is",self.balance)

        return
        

    def withdrawals(self,amount):
        if amount<50:
            print("you cant withdraw less than 50")

        elif amount<balance:
            print("you must have less than balance")
        else:
            self.balance-=amount
            self.withdrawals.append(amount)
        return

    def showdeposits(self,amount):
        if len(self.deposits)<1:
            print ("There are no deposits")
        else:
            self.deposits=amount

        for deposit in self.deposits:
            print("on",deposit['time'], "you deposited",deposit["amount"])
        return

    def showwithdrawals(self,amount):
        if len(self.withdrawals)<1:
            print("You cant withdraw less than you have deposited")

        for withdrawals in self.withdrawals:
            print("on",withdraw['time'], "you deposited", deposit["amount"])
        return

    def giveloans(self, amount):
        """
        Conditions for getting a loan:
            -User has made at least 10 deposits.
            -Loan requested is less than 1/3 of total data history.
            -User has no deposit balance.
            -User has no outstanding loans.
            -Loan has an interest on 10%
        The loan given is amount of outstanding loan 
        List
    
        List_of_deposits=[]
        for deposits in self.deposit:
            list of deposits.append
            for deposits in self.deposit:
        """


    amount = int(input("Please enter the amount:"))
    print(amount)

    if len(self.deposits)<10:
        print("Failed: You must have deposited at least 10 times")

    elif amount <50:
        print("Dear", self.name,'You cannot withdraw less than 50 bob')

    elif amount *3 >sum([Deposit['amount'] for deposit in self.deposits]):
        print("You do not have enough credit score")

    elif self.balance !=0:
        print("Youcannot have a balance before taking a loan")

    elif self.loan:
        print("You have an outstanding loan of ",self.loan)

    else:
        loan_interest = 0.1*amount
        loan_amount = amount + loan_interest
        self.loan +=loan_amount
        print("Success: You have received a loan of ", amount, "your outstanding loan balance is ", self.loan)
    

    def payloan(self,amount):
        """
        Accept loan payment if:
            - Amount is larger than zero
            - user has a loan or else save as deposit

        """
        return


