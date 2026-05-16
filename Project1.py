import random

computer = random.choice([1,2,3])
game = {1 : "Stone", 2 : "Paper", 3 : "Scissors"}
youstr = str(input("enter your choice "))
rev = { "stone": 1 , "paper": 2 , "scissors" : 3}
you = rev[youstr]

print(f"computer plays {game[computer]} and you plays {youstr}")

if(computer == you):
     print("Its a draw")
# else:
#     if(computer == 1 and you == 2): #-1
#         print("You win")
#     elif(computer == 1 and you == 3):# -2
#          print("you lose")
#     elif(computer == 2 and you == 3):# -1
#         print("you win")
#     elif(computer == 2 and you == 1):# -1
#          print("you lose")
#     elif(computer == 3 and you == 2):# 1
#          print("you lose")
#     elif(computer == 3 and you == 1):#2
#         print("you win")
       

else:  
          
    if((computer - you) == -1 or (computer - you )== 2):
     print("you win ")
    else:
     print("you lose")

