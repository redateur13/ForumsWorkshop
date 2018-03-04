import itertools

class MemberStore:	
	members = []
	last_id = 1

	def get_all(self):
		return MemberStore.members	

	def add(self, member):
		member.id = MemberStore.last_id
		MemberStore.members.append(member)
		MemberStore.last_id += 1
		
  
	def get_by_id(self, id):
		 member_list = self.get_all()
		 result = None
		 for member in member_list:
			 if member.id == id:
				 result = member
				 break
		 return result	
		 	    
	def delete(self, id):
		member = self.get_by_id(id)
		MemberStore.members.remove(member)	
				
		   
	def entity_exists(self, member):
		result = True
		if self.get_by_id(member.id) is None:
			result = False
		return result	
		
	def update(self, member):
		member_list = self.get_all()
		for index, this_member in enumerate(member_list):
			if this_member.id == member.id:
				member_list[index] = member
				
				
	def get_by_name (self, name):
		result = []
		member_list = self.get_all()
		for member in member_list:
			if member.name == name:
				result.append(member)
		return result
	
	def get_member_with_posts(self,all_posts):
		members = self.get_all()	
		for member,post in itertools.product(member_list,all_posts):	
			if member.id == post.member_id:
				member.all_posts.append(post)
			return members	
			 
	def get_top_two(self):
		members = self.get_all()
		members.sort(key=lambda member: len(member.posts), reverse=True)
		return members[:2]
		
class PostStore:
	posts = []
	last_id = 1
	
	def get_all(self):
		return PostStore.posts	
		
	 def add(self,post):
		 post.id = PostStore.last_id
		 PostStore.posts.append(post)
		 PostStore.last_id += 1
		
	
			 

