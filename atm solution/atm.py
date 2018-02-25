# allowed papers: 100, 50, 10, 5, 2, 1  
money = 500
request = (input ("enter you request : ")) 

try:
    request = int(request) 
    assert request > 0
except ValueError:
    print("your request must be a number !")

except AssertionError:
    print("your request is inferior or equal to 0 please try again")
 
if request <= money :
	while request >= 100 :
		print ("give 100")
		request -= 100
	
	while request >= 50	:
		print ("give 50")
		request -= 50
	
	while request >= 10 :
		print ("give 10")
		request -= 10
	
	while request >= 5 :
		print ("give 5")
		request -= 5	

	while request >= 2 :
		print ("give 2")
		request -= 2
	
	while request >= 1 :
		print ("give 1")
		request -= 1	
else:
	print (" sorry , your request must be inferior or equal to " ,money )		



