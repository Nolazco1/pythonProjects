# This program lets you play rock,
# paper, scissors against the computer.

import random

# Gets computer's choice
comp_choice = random.randint(1, 3)

def main():
    while True:
        # Get player's guess
        print('Rock, Paper, or Scissors?')
        print('1 = Rock, 2 = Paper, 3 = Scissors')
        choice = int(input())
        # Results
        if choice == comp_choice:
            print("You both picked the same style, it's a draw.")
        elif choice == 1 and comp_choice == 3:
            print('Rock beats scissors, you won.')
        elif choice == 3 and comp_choice == 1:
            print('Rock beats scissors, Computer won.')
        elif choice == 1 and comp_choice == 2:
            print('Paper beats Rock, Computer won.')
        elif choice == 2 and comp_choice == 1:
            print('Paper beats Rock, you won.')
        elif choice == 2 and comp_choice == 3:
            print('Scissors beats paper, Computer won.')
        elif choice == 3 and comp_choice == 2:
            print('Scissors beats paper, you won.')

# Run the main function
main()
        
            
            
        
    
