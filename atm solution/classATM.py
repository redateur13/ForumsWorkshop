class ATM:
	'''class ATM to use with multiple ATM Bank '''
	def __init__(self, balance, bank_name):
		self.balance = balance
		self.bank_name = bank_name
 
	def withdraw(self, request):
		''' atm solution with function 
		allowed papers: 100, 50, 10, 5.'''
		print("Welcome to " + self.bank_name)
		result = self.balance
		if request > self.balance:
			print("Can't give you all this money !")
		elif request <= 0:	
			print("The request is invalid amount !")	
		else :
			result -= request
			while request > 0 :
				if request >= 100 :
					print ("give 100")
					request -= 100
				elif request >= 50:
					print ("give 50")
					request -= 50
				elif request >= 10 :
					print ("give 10")
					request -= 10	
				elif request >= 5 :
					print ("give 5")
					request -= 5
				elif request <= 4 :
					print ("give " , request)
					request = 0
		return result  
						

balance1 = 500
balance2 = 1000
		
atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

print (atm1.withdraw(257))

print (atm2.withdraw(374))

