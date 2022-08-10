'''
Number Guessing 
This project is a fun game that generates a random number in a certain specified range and the user must guess the number after receiving hints. 
Every time a user’s guess is wrong they are prompted with more hints to make it easier — at the cost of reducing the score.

The program also requires functions to check if an actual number is entered by the user, and finds the difference between the two numbers. 
'''
import random


random_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
 
hidden_num = random.choice(random_num)

end_game = False 
guess_time = 0

while end_game == False  :
    if guess_time < 3 :
        guessed_num = int(input("Guess the hidden number: "))

        if guessed_num > hidden_num:
            guess_time += 1
            end_game = False
            if guess_time <= 2 :
                print("guess a lower number")


        elif guessed_num < hidden_num:
            guess_time += 1
            end_game = False
            if guess_time <= 2 :
                print("guess a higher number")


        else:
            print("congratulation you guessed the right number")
            end_game = True
            hidden_num = random.choice(random_num)
            guess_time += 1
            if end_game == True :
                start_again = input("Do you want to start again 'yes' or 'no' ")
                if start_again == 'yes' :
                    end_game = False
                    hidden_num = random.choice(random_num)
                    guess_time = 0
                else :
                    end_game = True

    else :
        end_game = True
        print ('You are out of guesses')
        print(f'The hidden number is {hidden_num}')

        if end_game == True :
            start_again = input("Do you want to start again 'yes' or 'no' ")
            if start_again == 'yes' :
                end_game = False
                hidden_num = random.choice(random_num)
                guess_time = 0
            else :
                end_game = True

