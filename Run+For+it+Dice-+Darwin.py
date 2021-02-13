##=========================================================
##  Program: Run for it Dice
##  Author: Darwin Liao
##  Date: 3/28/2017
##  Description: A dice game to help children learn about
##                  series and patterns
##               
##   
##=========================================================
from random import randrange
playerAmount = int(input("How many people are playing?: "))
diceAmount = int(input("How many dice?: "))
scoreLimit = int(input("What is the Score you want to play to?: "))
score = [0]*playerAmount
player = 0
diceNum = []
combos = []

#=====================================#
#   This Portion is where all the
#          calulations occur
#=====================================#

#A function to subtract dice from the catalog.
def subDice(diceNum, n, amt):
    for x in range(n, n+amt):
        diceNum[x] -= 1
        
#Resets all of the information / deletes the information.
def reset(info):
    while(info!= []):
        del info[-1]
#Generates Random Dice
def genDice():
    rolls = [randrange(1,7) for x in range(diceAmount)]
    print("The dice rolls are: " + str(rolls))
    print()
    #Adds the values of the dice into a catalog instead of a large list of dice.
    for i in range(1,7):
        diceNum.append(rolls.count(i))
    print("It is now player " + str(player + 1) + "'s turn")
    #Resets the lists for the next calculation
    reset(rolls)

#Calculates the maximum possible score where diceNum is an array of the AMOUNT of each number of dice
def maxScore(diceNum):
    cScore = 0
    #Goes through the catalog of dice and checks if there is a pair of dice
    #if there is, add the pair to a list and take away one from each section of
    #the catalog          
    for n in range(len(diceNum)-1):
        for m in range(diceNum[n]):
            if diceNum[n]>0 and diceNum[n+1] >0:
                subDice(diceNum, n, 2)
                combos.append([n+1,n+2])             
    #Checks if there are any leftover dice that have not been paired. If there are,
    #Add them to the end of a possible pair to have a combonation
    for y in range(len(diceNum)):
        if(diceNum[y]>0):
            for x in range(len(combos)):
                if combos[x][-1] == y and diceNum[y] > 0:
                    combos[x].append(y+1)
                    diceNum[y] -= 1
    #Calculates the Correct score and places it into the variable cScore (comboScore)
    for x in combos:
        cScore += len(x)*5
    #Resets the lists for the next calculation
    reset(diceNum)
    reset(combos)
    return cScore

#===============================================#
#         This Portion is for the player's
#              win checking and turns
#===============================================#

#checks to see if any player has won yet.        
while(max(score) < scoreLimit):
    for player in range(playerAmount):
        genDice()
        guess = int(input("What is the maximum score?: "))
        correctScore = maxScore(diceNum)
        #Asks the player to guess. If the player guesses right, he gets the current score added to his score
        if guess == correctScore:
            print("Correct!")
            score[player] += correctScore
            print("Player " + str(player + 1) + "'s score is: " + str(score[player]))
            print()
        else:
            print("Wrong!")
            print("Player " + str(player + 1) + "'s score is: " + str(score[player]))
            print()  


#Adds the winners into an array to print out if there is a tie or not
winners = []      
for x in range(len(score)):
    if score[x] >= scoreLimit:
        winners.append("Player " + str(x + 1))
if (len(winners) > 1):
    print("Tie! "+ " and ".join(winners) + " Tied!")
else:
    print("".join(winners) + " Won!")
    
