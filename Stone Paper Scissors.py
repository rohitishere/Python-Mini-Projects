play_again="Yes"

actions=["Rock","Paper","Scissor"]

while play_again=="Yes":

  computer_choice=random.choice(actions)


  player_choice=input("Enter your action:(Rock/Paper/Scissor)")
  print("The computer's action is:",computer_choice)

  if computer_choice==player_choice:
    print("Both have chose",computer_choice,"It's a Tie!")
  elif computer_choice=="Rock" and player_choice=="Scissor":
    print("The Rock has smashed the Scissor..Alas! The player lose.")
  elif computer_choice=="Rock" and player_choice=="Paper":
    print("The Paper has covered the Rock..Congrats! The player won.")
  elif computer_choice=="Paper" and player_choice=="Scissor":
    print("The Scissor has cut the Paper..Congrats! The player won.")
  elif computer_choice=="Paper" and player_choice=="Rock":
    print("The Paper has covered the Rock..Alas! The player lose.")
  elif computer_choice=="Scissor" and player_choice=="Paper":
    print("The Scissor has cut the Paper..Alas! The player lose.")
  elif computer_choice=="Scissor" and player_choice=="Rock":
    print("The Rock has smashed the Scissor..Congrats! The player won.")

  play_again=input("Do you want to play again?(Yes/No): ")
