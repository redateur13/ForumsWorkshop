def withdraw(request, balance):
	''' atm solution with function 
	    allowed papers: 100, 50, 10, 5.'''
	result = balance
	if request > balance:
			print("Can't give you all this money !")
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
				print ("give " + str(request))
				request = 0
	return result  
				                               	    			
balance = 500	
balance = (withdraw(357, balance))	
	
print (balance)

