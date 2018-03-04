class Member:
	def __init__(self, name , age):
		self.member_id = id
		self.name = name
		self.age = age
		self.posts = []
		
	def __str__(self):
		return 'Name: {}\t\tAge: {}'.format(self.name, self.age)
        	

class Post:
	'''define a title and topic of post '''
	def __init__(self, title , topic, member_id):
		self.id = 0
		self.title = title
		self.topic = topic
		self.member_id = member_id
		
	def __str__(self):
		return 'Title : {}\t\tPost: {}'.format(self.title, self.topic)	 
	
