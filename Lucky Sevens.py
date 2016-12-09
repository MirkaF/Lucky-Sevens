##Lucky Sevens

#--------------------------------------------------------------#
#Start with $10, every game costs $1 to play
#Roll two dice
#If the result is seven, win $5 (+$4 overall after the $1 cost) 
#The game continuously play until you run out of money.
#At the end, it tells you how many rounds were played.

#--------------------------------------------------------------#
import random
import sys
money = 10
turn = 0
while money!=0
dice1 = random.randint (1, 6)
dice2 = random.randint (1, 6)
total = dice1 + dice2