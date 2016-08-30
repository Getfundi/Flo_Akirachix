class MPESA:
	def __init__(self,name,number):
		 self.name=name
		 self.number=number
		 self.balance=0.0
		 self.deposit=[]
		 self.deposit=[]
		 print("welcome",self.name)

	def deposit(self,amount):
		if amount<50:
			print("You cannot deposit less than 50")
		else:
			self.deposit.append(amount)
			self.balance+=amount
			print("Dear",self.name, "you have deposited", amount,"your new balance is",self.balance)
		return
		
	def withdraw(self,amount):
		if amount<50:
			print("You cant withdraw less than 50 ")
		elif self.balance<amount:
			print("You must have enough balance")

		else:
			self.withdrawal.append(amount)
			self.balance-=amount
			print("Dear",self.name,"You have withdrawn", amount,"your new balance is",self.balance)
		return
	def showDeposits(self):
		if len(self.deposits)<1:
			print("You have not made any deposits")
		else:
			for deposit in self.deposits:
				print(deposit)

	






