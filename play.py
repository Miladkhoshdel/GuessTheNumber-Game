# Created By Milad Khoshdel for fun

import random


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
