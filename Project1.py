# Snake,Water,Gun Game : 
'''
1 for snake
-1 for water
0 for gun
'''

import random # This is my random module and ye hum  ne es leya chose keya hai taki humm random number generate kar saka in comuter variable.

computer = random.choice([-1,0,1]) # to assign random value in computer variable we use "random module"  
you = input("Enter your choice : ")
yourDict = {
    "snake": 1,
    "water": -1,
    "gun": 0
}
reverseyourDict = {
    1: "snake",
    -1: "water",
    0: "gun"
}

yourchoice = yourDict[you]

print(f"You chose: {reverseyourDict[yourchoice]} \nComputer chose: {reverseyourDict[computer]} ")

if(computer == yourchoice):
    print("It's a Draw!")

elif(computer == -1 and yourchoice == 1):
    print("You Win!")

elif(computer == -1 and yourchoice == 0):
    print("You Lose!")

elif(computer == 1 and yourchoice == 0):
    print("You Win!")

elif(computer == 1 and yourchoice == -1):
    print("You Lose!")

elif(computer == 0 and yourchoice == 1):
    print("You Lose!")

elif(computer == 0 and yourchoice == -1):
    print("You Win!")

else:
    print("Something went wrong")