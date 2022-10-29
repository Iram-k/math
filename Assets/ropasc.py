import random

user=input("Enter a choice : (rock,paper,scissors)")
pos=["rock","paper","scissors"]
comp=random.choice(pos)
print("computer's choice :",comp)

# print user action and computer action
if user==comp:
    print("tie")
elif user=="rock" and comp=="scissors":
    print("user wins")
elif user=="scissors" and comp=="paper":
    print("user wins")
elif user=="paper" and comp=="rock":
    print("user wins")
else:
    print("computer wins")
