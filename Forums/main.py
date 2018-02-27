
import models 
import store 

member1 = models.Member("reda" , 27)
member2 = models.Member("amine" , 18)


post1 = models.Post("function Print in Python " , "The print statement has ...")
post2 = models.Post("python input " , "Input can come in various ..." )
post3 = models.Post("exercise " , "Create a program that asks the user ...")


print(member1.name)
print(post1.title)
print(post1.topic)

print(member2.age)
print(post2.title)
print(post3.topic)

member_stored = store.MemberStore()
member_stored.add(member1)
member_stored.add(member2)

print(member_stored.get_all)
