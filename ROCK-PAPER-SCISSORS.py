'''
first we have to calculate everything to matematical format
1 for rock 
-1 for paper
0 for scissors
'''
import random
computer = random.choice([-1,1,0])
# computer = -1
youstr = input('''
r for rock 
p for paper
s for scissors
"Enter your choice: ''')
# print(f"you chooose{reversedict[you]} and computer chooses{computer}")

youdict = { "r" : 1,"p" : -1, "s" : 0}
reversedict = {1: "ROCK", 0 : "SCISSORS", -1:"PAPER"}
you = youdict[youstr]
print(f"you chooose {reversedict[you]} and computer chooses {reversedict[computer]}")
#when computer chooses rock (1)
if(computer==you):
    print("Match tie")

else:
    #when computer chooses 1 (rock)
    if(computer==1 and you==-1):
        print("you win") 
    elif(computer==1 and you==0):                 
        print("computer win")
#when computer chooses paper (-1)
    elif(computer==-1 and you==0):
        print("you win")
    elif(computer==-1 and you==1):
        print("computer win")
#when computer chooses scissors (0)
    elif(computer==0 and you==1):
        print("you win")
    elif(computer==0 and you==-1):
        print("computer win")
    else:
        print("something went wrong")