from models import *

member1 = Member("reda" , 27)
member2 = Member("amine" , 18)


post1 = Post("function Print in Python " , "The print statement has ...")
post2 = Post("python input " , "Input can come in various ..." )
post3 = Post("exercise " , "Create a program that asks the user ...")


print(member1.name)
print(post1.title)
print(post1.topic)

print(member2.age)
print(post2.title)
print(post3.topic)
