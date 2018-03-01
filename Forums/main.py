import models 
import store 

def create_members():
	member1 = models.Member("reda" , 27)
	member2 = models.Member("amine" , 18)

	
	return member1, member2
	
def creat_posts():	
	post1 = models.Post("function Print in Python " , "The print statement has ...")
	post2 = models.Post("python input " , "Input can come in various ..." )
	post3 = models.Post("exercise " , "Create a program that asks the user ...")
	print(post1.title)
	print(post2.title)
	print(post3.topic)
	
	return post1, post2, post3
	
	
def add_members_to_store(members_instances, member_stored):
	for member in members_instances:
		member_store.add(member)
		
def print_all_members(member_store):
	print("=" * 20)
	
	for member in member_store.get_all():
		print(member)
	print("=" * 20)		
	
def update_object(member_store, member2):
	member2_copy = models.Member(member2.name, member2.age)
	member2_copy.id = 3

	if member2_copy is not member2:
		print("member2 and member2_copy are not the same !")	
		member2_copy.name = "john"
		member_store.update(member2_copy)
		
members_instances = create_members()
member1, member2 = members_instances

member_store = store.MemberStore()

add_members_to_store(members_instances, member_store)

print_all_members(member_store)

update_object(member_store, member2)

	

	
