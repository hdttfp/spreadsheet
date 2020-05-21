import random


def rps():
    choice_number = random.randint(1, 3)
    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'paper'
    elif choice_number == 3:
        choice = 'scissors'
    return choice


my_choice = input('Choose rock, paper, scissors.')
opponent_choice = rps()


print('You chose {}. Your opponent chose {}.'.format(my_choice, opponent_choice))

if my_choice == 'rock' and opponent_choice == 'paper':
    print('You lose!')
elif my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')
elif my_choice == 'paper' and opponent_choice == 'scissors':
    print('You lose!')
elif my_choice == 'paper' and opponent_choice == 'rock':
    print('You win!')
elif my_choice == 'scissors' and opponent_choice == 'rock':
    print('You lose!')
elif my_choice == 'scissors' and opponent_choice == 'paper':
    print('You win!')
elif my_choice == opponent_choice:
    print('Draw!')
