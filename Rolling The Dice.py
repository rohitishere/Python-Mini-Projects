import random

print("-----Dice Simulator-----")

x="y"

while(x=="y" or x=="yes"):

  n=random.randint(1,6)

  if n==1:
    print("Rolling the Dices....")
    print("[------]")
    print("[      ]")
    print("[  0   ]")
    print("[      ]")
    print("[------]")
    print("The dice value is ",n)
    

  elif n==2:
      print("Rolling the Dices....")   
      print("[------]")
      print("[0     ]")
      print("[      ]")
      print("[     0]")
      print("[------]")
      print("The dice value is ",n)


  elif n==3:
      print("Rolling the Dices....")
      print("[------]")
      print("[0     ]")
      print("[  0   ]")
      print("[     0]")
      print("[------]")
      print("The dice value is ",n)
      


  elif n==4:
      print("Rolling the Dices....")
      print("[------]")
      print("[0    0]")
      print("[      ]")
      print("[0    0]")
      print("[------]")
      print("The dice value is ",n)
      


  elif n==5:
      print("Rolling the Dices....")
      print("[------]")
      print("[0    0]")
      print("[  0   ]")
      print("[0    0]")
      print("[------]")
      print("The dice value is ",n)
      


  elif n==6:
      print("Rolling the Dices....")
      print("[------]")
      print("[0    0]")
      print("[0    0]")
      print("[0    0]")
      print("[------]")
      print("The dice value is ",n)
      

  x=input("Do you want to roll the dice more?(yes/no):")
