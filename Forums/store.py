class MemberStore:	
	members = []
	last_id = 1

	def get_all(self):
		# get all members
		return MemberStore.members

	def add(self, member):
		# append member
		member.id = MemberStore.last_id
		MemberStore.members.append(member)
		MemberStore.last_id += 1
      
  
	def get_by_id(self, id):
		 member_list = self.get_all()
		 for member in member_list:
			 if member.id == id:
				 return member
		 return None		 

	   
	def delete(self, id):
		# delete member by id
		for member in self.get_all():
			if member is not None:
				MemberStore.members.remove(member)
		
		   
	def entity_exists(self, member):
		# checks if an entity exists in a store
		result = True
		if self.get_by_id(member.id) is None:
			result = False
		return result
