#1 This is my first project: Rock, Paper, Scissors
print('Hello welcome to Rock, Paper Scissors')

#9 Adding a score counter
user_score = 0
computer_score = 0

#7 Adding the option to play again
repeatgame = True
while repeatgame == True:

#2 Firstly, need an input from the user
    RPS_choice: str = input('Please enter: \"Rock\", \"Paper\", or \"Scissors\": ').capitalize()

#6 Ensuring the user enters a valid input
    while RPS_choice != 'Rock' and RPS_choice != 'Paper' and RPS_choice != 'Scissors':
        RPS_choice: str = input('Invalid choice. Please enter: \"Rock\", \"Paper\", or \"Scissors\": ').capitalize()

#5 Making sure game repeats in "Draw" case
    draw = True
    while draw == True:

#3 Creating computer choices
        computer_options = ['Rock', 'Paper','Scissors']
        import random
        choice_randomiser = random.randint(0,2)
        computer_choice = computer_options[choice_randomiser]
        print(f'Computer has chosen: \"{computer_choice}\"')

#4 Determing the winner
        if RPS_choice == computer_choice:
            print("Draw!")
            RPS_choice: str = input('Please enter \"Rock\", \"Paper\", or \"Scissors\" again: ').capitalize()
        elif RPS_choice == 'Rock' and computer_choice == 'Paper':
            computer_score += 1
            print('You lose!')
            draw = False
        elif RPS_choice == 'Rock' and computer_choice == 'Scissors':
            user_score += 1
            print('You win!')
            draw = False
        elif RPS_choice == 'Paper' and computer_choice == 'Scissors':
            computer_score += 1
            print('You lose!')
            draw = False
        elif RPS_choice == 'Paper' and computer_choice == 'Rock':
            user_score += 1
            print('You win!')
            draw = False
        elif RPS_choice == 'Scissors' and computer_choice == 'Rock':
            computer_score += 1
            print('You lose!')
            draw = False
        elif RPS_choice == 'Scissors' and computer_choice == 'Paper':
            user_score += 1
            print('You win!')
            draw = False
    print('Thank you for playing!')
    play_again: str = input('Do you want to play again? Please enter \"Yes\" or \"No\": ').capitalize()

#8 Ensuring valid input again
    while play_again != 'Yes' and play_again != 'No':
        play_again: str = input('Invalid response. Please enter \"Yes\" or \"No\": ').capitalize()
    if play_again == 'Yes':
        repeatgame = True
    else:
        print(f'The final score is You: {user_score}, Computer: {computer_score}')

#10 Adding a final winner evaluation
        if user_score == computer_score:
            print('Overall, the game was drawn :| ')
        elif user_score > computer_score:
            print('Overall, you win the game :) ')
        else:
            print('Overall, you lose the game :( ')
        print('Goodbye, look forward to playing with you again!')
        repeatgame = False
#hiihih






