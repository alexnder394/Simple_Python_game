from random import randint
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

print("*** Rock *** Paper *** Scissors ***\n")
player=input("Player, make your move: ").lower()

if player == "rock" or player == "paper" or player == "scissors":
		print(f"computer plays: {computer}")
		if player == computer:
			print("even, play again!")
		elif player == "rock":
			if computer == "paper":
				print("computer wins!")
			else:
				print("Player wins!")
		elif player == "paper":
			if computer == "rock":
				print("Player wins!")
			else:
				print("computer wins!")
		elif player == "scissors":
			if computer == "paper":
				print("Player wins!")
			else:
				print("computer wins!")
		else:
			print("Please enter a valid choice, \"rock\" or \"paper\" or \"rock\"")
else:
	print("You must enter a valid choice, \"rock\" or \"paper\" or \"scissors\"")