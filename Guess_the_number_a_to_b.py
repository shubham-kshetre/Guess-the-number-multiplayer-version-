#  Problem Statement:-
# Generate a random integer from a to b.
#  You and your friend have to guess a number between two numbers, a and b.
#  a and b are inputs taken from the user. Your friend is player 1 and plays first.
#  He will have to keep choosing the number, and 
# your program must tell whether the number is greater than the actual number or less than
#  the actual number. Log the number of trials it took your friend to arrive at the number. 
# You play the same game, and then the person with the minimum number of trials wins! 
# Randomly generate a number after taking a and b as input and don’t show that to the user.

import random #to get random number
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

player1 = input("Enter name of Player 1: ")
player2 = input("Enter name of Player 2: ")

def play(player_name):
    for i in range(1,6): # 6 because for each player there will be 5 chances 
        print(f"You have {6-i} trials left.")
        player = int(input(f"Enter number from {a} to {b} {player_name}: "))
        
        if player == random_num:
            print(f"{player_name} You Guess right..!")
            print(f"{player_name} guessed in {i} guesses.")
            break
        elif player < random_num:
            print(f"Your guess is smaller than the number\nTry again")
        elif player > random_num:
            print(f"Your guess is greater than the number\nTry again") 

  

game_number = 1 #it will help to know how many times you played the game

while True: #this loop is work as main source code because all the fun will be called from this loop
    print(f"It's {player1}'s turn")
    to_start = input("Press 'b' to begin: ")
    if to_start == "b":  #i don't know how to do it with "press any key"
        random_num = random.randint(a,b)
        play(player1)
    
    print(f"Now {player2}'s turn")
    to_start = input("Press 'b' to begin: ")
    if to_start == "b":
        random_num = random.randint(a,b) #it will generate second random number
        play(player2)
      
    for_next_game = input("Do you want to play again guys? (y/n)")
    if for_next_game=="y":
        game_number = game_number + 1
        sign = "="*5 #it is just to know that new game begins from here
        print(f"{sign} GAME NUMBER {game_number} {sign}")
        continue
    else:
        print(f"You played {game_number} times")
        exit()

    





