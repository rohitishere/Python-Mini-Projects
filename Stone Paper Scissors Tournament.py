n=int(input("Enter the number of matches you want to play :"))

actions=["Rock","Paper","Scissor"]

computer_points=0
player_points=0

for i in range(n):
  computer_choice=random.choice(actions)
  player_choice=input("Enter your Action(Rock/Paper/Scissor):")



  if computer_choice==player_choice:
    print("Both have chose",computer_choice,"It's a Tie!")
  elif computer_choice=="Rock" and player_choice=="Scissor":
    print("The Rock has smashed the Scissor..Alas! The player lose.")
    computer_points+=1
  elif computer_choice=="Rock" and player_choice=="Paper":
    print("The Paper has covered the Rock..Congrats! The player won.")
    player_points+=1
  elif computer_choice=="Paper" and player_choice=="Scissor":
    print("The Scissor has cut the Paper..Congrats! The player won.")
    player_points+=1
  elif computer_choice=="Paper" and player_choice=="Rock":
    print("The Paper has covered the Rock..Alas! The player lose.")
    computer_points+=1
  elif computer_choice=="Scissor" and player_choice=="Paper":
    print("The Scissor has cut the Paper..Alas! The player lose.")
    computer_points+=1
  elif computer_choice=="Scissor" and player_choice=="Rock":
    print("The Rock has smashed the Scissor..Congrats! The player won.")
    player_points+=1


print("Player Points = ",player_points)
print("Computer Points = ",computer_points)

if player_points>computer_points:
  print("Great!! The player won the Series..")
elif player_points==computer_points:
  print("The Series is Drawn..Well Played both the Teams!!")
else:
  print("Ah! The player lose the Series..")
