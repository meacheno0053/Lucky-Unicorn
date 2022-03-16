import random

# main routine goes here

tokens = ["unicorn", "horse", "horse", "horse", "zebra", "zebra", "zebra",  "donkey", "donkey", "donkey", "donkey"]
STARTING_BAlANCE = 100
balance = STARTING_BAlANCE

# Testing loop to generate 20 tokens 
for item in range (0,500):
  chosen = random.choice(tokens)

  # Adjust balance 
  if chosen == "unicorn":
    balance += 4
  elif chosen == "donkey":
    balance -= 1
  else:
    balance -= 0.5


print()
print("starting balance: ${:.2f}".format(STARTING_BAlANCE))
print ("final balance: ${:.2f}".format(balance))
