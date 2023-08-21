#Ransford Addai(Individual Project)
#Number Guessing Game


import random

def number_guessing_game():
    print("Welcome To our number Guessing Game👋")
    print()
    correct_number = random.randint(1,50)
    number_of_attempts = 0
    maximum_attempts = 7

    while number_of_attempts< maximum_attempts:
        try:
            player_Guess = int(input("Guess a number correctly: "))
        except ValueError:
            print("Please enter a valid number😊")
            continue

        number_of_attempts += 1

        if player_Guess == correct_number:
            print(f"Congratulations! You chose {correct_number} after {number_of_attempts} attempts")
            return
        elif player_Guess < correct_number:
            print("Too Low, Please come up little further. ")
        else:
            print("Too High, Please come up. ")


    print("You have used all your chances. You Lose😂. ")


if __name__ == '__main__':
    number_guessing_game()