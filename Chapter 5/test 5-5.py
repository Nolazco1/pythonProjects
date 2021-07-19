def main():
    from random import randint
    UserChoices = input("'rock', 'paper' or 'scissors'? \n Input: ")
    if UserChoices == "rock":
        UserChoice = 1
    elif UserChoices == "paper":
        UserChoice = 2
    elif UserChoices == "scissors":
        UserChoice = 3
    CpuChoice = randint(1,3) 
    if UserChoice == CpuChoice:
        print("DRAW!")
    elif UserChoice == 1 and CpuChoice== 3:
        print("Rock beats scissors PLAYER WINS!")
        main()
    elif UserChoice == 3 and CpuChoice== 1:
        print("Rock beats scissors CPU WINS")
        main()
    elif UserChoice == 1 and CpuChoice== 2:
        print("Paper beats rock CPU WINS!")
        main()
    elif UserChoice == 2 and CpuChoice== 1:
        print("paper beats rock PLAYER WINS!")
        main()
    elif UserChoice == 2 and CpuChoice== 3:
        print("Scissors beats paper CPU WINS!")
        main()
    elif UserChoice == 3 and CpuChoice== 2:
        print("Scissors beats paper PLAYER WINS!")
        main()
    elif UserChoice == 1 and CpuChoice== 2:
        print("cpu wins")
        main()
    else:
        print("Error: outcome not implemented")
main()
