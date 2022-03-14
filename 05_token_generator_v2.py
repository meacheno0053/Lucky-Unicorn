import random

# main routine goes here

tokens = ["unicorn", "horse", "zebra", "donkey"]

# Testing loop to generate 20 tokens
for item in range (0,20) :
  chosen = random.choice(tokens)

  #ajust balance
  if chosen == "unicorn":
   balance += 4
  elif chosen == "donkey":
    balance -= 1
  else: 
    balance -= 0.5

# output
print ("token: {} , Balance: ${}".format(chosen, balance))