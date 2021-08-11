replay="Yes"

while(replay=="Yes" or replay=="yes"):

  dice1=random.randint(1,6)
  print("The outcome of Dice 1:",dice1)
  dice2=random.randint(1,6)
  print("The outcome of Dice 2:",dice2)
  print("The sum of the outcome of the dice is:",(dice1+dice2))

  if (dice1+dice2) == 7 or (dice1+dice2) == 11:
    player="win"
  else:
    player="lose"

  if player=="win":
    print("Congrats! You won the match")
  else:
    print("Sorry! You lose the match")
  replay=input("Do you want to play again?(Yes/No):" )
