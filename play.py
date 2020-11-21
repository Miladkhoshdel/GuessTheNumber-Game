# Created By Milad Khoshdel for fun

import random

mode = int(input("Please choose the game mode:\n1- Computer choose a number and you try to guess it.\n2- You choose a number and computer try to guess it. \nWhat is your choice ? "))

if mode == 1:
    name = input("\nPlease Enter Your Name: ")
    print("\nHi", name + ",")

    play_again = True
    while play_again:
        number = random.randint(1,99)
        print("I choosed a number between 0 and 100. can you guess wat is it ?")
        guess = int(input("\nPlease Choose a number: "))

        while (number != guess):
            if guess < number:
                guess = int(input("Please Choose bigger number: "))
            else:
                guess = int(input("Please Choose smaller number: "))
            
        print("WoW", name + ". You won the Game. The number is", number)
        again = input("\nDo you want to play again ? ")
        if again == "no":
            play_again = False
else:
    name = input("\nPlease Enter Your Name: ")
    print("\nHi", name + ",")

    play_again = True
    while play_again:
        print("Select a number between 0 to 100 and i try to guess what is it.")
        number = int(input("\nPlease Choose a number: "))
        print("Please help me. if my guess is bigger than your number select 'b' and if it's smallers, select 's'.")
        a = 0
        b = 100
        guess = random.randint(a,b)
        while guess != number:
            print("Is the number", guess, "?")
            guide = input("b/s ? " )
            if guide == "b":
                a = guess
                guess = random.randint(a,b)
            else:
                b = guess
                guess = random.randint(a,b)
        print("WoW", name + ". You won the Game. The number is", number)
        again = input("\nDo you want to play again ? ")
        if again == "no":
            play_again = False
        
