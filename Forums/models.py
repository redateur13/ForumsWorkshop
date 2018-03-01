class Member:
	'''define a member name and age '''
	def __init__(self, name , age):
		self.member_id = id
		self.name = name
		self.age = age
		
	def __str__(self):
		return 'Name: {}\t\tAge: {}'.format(self.name, self.age)
        	

class Post:
	'''define a title and topic of post '''
	def __init__(self, title , topic):
		self.title = title
		self.topic = topic 
	
