import models 
import store 

def create_members():
	member1 = models.Member("reda" , 27)
	member2 = models.Member("amine" , 18)
	member3 = models.Member("zaki", 25)

	
	return member1, member2, member3
	
def creat_posts():	
	post1 = models.topic("function Print in Python " , "The print statement has ...")
	post2 = models.topic("python input " , "Input can come in various ..." )
	post3 = models.topic("exercise " , "Create a program that asks the user ...")
	print(post1)
	print(post2)
	print(post3)
	
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
		
def store_should_get_members_with_posts(member_store, post_store):
	members = member_store.get_member_with_posts(post_store.get_all())
	for member in members:	
		print ("%shas posts:" % member)	
		for post in member.member_posts:
			print ("\t%s" % post)
		
members_instances = create_members()
member1, member2, member3 = members_instances


member_store = store.MemberStore()

add_members_to_store(members_instances, member_store)

print_all_members(member_store)

update_object(member_store, member2)


def store_should_add_posts(posts_instances, post_store):
    for member in posts_instances:
        post_store.add(member)


def store_should_get_members_with_posts(member_store, post_store):
    members_with_posts = member_store.get_members_with_posts(post_store.get_all())

    for member_with_posts in members_with_posts:
        print(f"{member_with_posts} has posts:")
        for post in member_with_posts.posts:
            print(f"\t{post}")

        print("=" * 10)


def store_should_get_top_two(member_store, post_store):
    top_two_members = member_store.get_top_two(post_store.get_all())

    for member_with_posts in top_two_members:
        print(f"{member_with_posts} has posts:")
        for post in member_with_posts.posts:
            print(f"\t{post}")

members_instances = create_members()
member1, member2, member3 = members_instances

member_store = store.MemberStore()




	


	

	
