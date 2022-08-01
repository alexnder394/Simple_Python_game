from random import randint
print("*** Rock *** Paper *** Scissors ***\n")
player_wins = 0
computer_wins = 0
winning_score = 3

while computer_wins < winning_score and player_wins < winning_score:
    print(f"Player Score: {player_wins} \nComputer Score: {computer_wins}\n")
    player = input("Player, make your move: ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    if player == "rock" or player == "paper" or player == "scissors":
        print(f"computer plays: {computer}")
        if player == computer:
            print("even, play again!")
        elif player == "rock":
            if computer == "paper":
                print("computer wins!")
                computer_wins += 1
            else:
                print("Player wins!")
                player_wins += 1
        elif player == "paper":
            if computer == "rock":
                print("Player wins!")
                player_wins += 1
            else:
                print("computer wins!")
                computer_wins += 1
        elif player == "scissors":
            if computer == "paper":
                print("Player wins!")
                player_wins += 1
            else:
                print("computer wins!")
                computer_wins += 1
        else:
            print("Please enter a valid choice, \"rock\" or \"paper\" or \"rock\"")
    else:
        print("You must enter a valid choice, \"rock\" or \"paper\" or \"scissors\"")
if player_wins > computer_wins:
    print("Congrats, you won!")
elif player_wins == computer_wins:
    print("It's a tie!")
else:
    print("Computer won! Better luck next time!")
