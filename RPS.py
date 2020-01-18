import random
player1 = input("Player 1: rock, paper, or scissors ")
a = random.randint(0,2)
if a==0:
   player2="rock"
elif a==1:
   player2="paper"
else:
   player2="scissors"
print("Computer chooses "+ player2)
if player1 == "rock" and player2 == "scissors":
	print("player1 wins!")
elif player1 == "rock" and player2 == "paper":
	print("Computer wins!")
elif player1 == "paper" and player2 == "rock":
	print("player1 wins!")
elif player1 == "paper" and player2 == "scissors":
	print("Computer wins!")
elif player1 == "scissors" and player2 == "rock":
	print("Computer wins!")
elif player1 == "scissors" and player2 == "paper":
	print("player1 wins!")
elif player1 == player2:
	print("It's a tie!")
else:
	print("something went wrong")
