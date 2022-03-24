import random

def yes_no (question):
  valid = False
  while not valid:
    response = input(question).lower()
    
    if response == "yes" or response == "y": 
      # print("you chose yes")
      return "yes"
    
    elif response == "no" or response == "n": 
      return "no"
    
    else:
      print("Please answer yes / no")

   

def instructions ():
  print("**** How to Play ****")
  print()
  print("The rules of the game go here")
  print()
  return ""

# checks for a number between low and high
def num_check(question, low, high ):
  error = "Please enter an whole number between 1 and 10\n"
  
  valid = False
  while not valid: 
    try:
      # ask the question 
      response = int(input(question))
    
      # if the amount is too low / too high give
      if low < response <= high:
        return response
    
    # output an error
      else: 
        print(error)
  
    except ValueError:
      print(error)
      

# ******* Main routine starts here ******
played_before = yes_no("Have you played before? ")

if played_before == "no":
  instructions()

# print("program continues")

how_much = num_check ("How much would you like to play with? " , 0, 10 )

print("You will be spending ${}".format (how_much))

balance = how_much

rounds_played = 0

play_again = ""
while play_again == "":

  # play_again = input ("press <Enter> to play...").lower()

    #increase # of rounds played
  rounds_played += 1

  # print round number
  print()
  print("*** Round #{} ***".format(rounds_played))
  chosen_num = random.randint (1, 100)
  
  # Adjust balance
  # if the random # is between 1 and 5,
  # user gets a unicorn (add $4 to balance)
  if 1 <= chosen_num <= 5:
    chosen = "Unicorn"
    balance += 4
    
    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
  elif 6 <= chosen_num <= 36:
    chosen = "Donkey"
    balance -= 1

    # the token is either horse or zebra
    # in both cases, subtract $0.50 from the balance
  else:
    if chosen_num % 2 ==0:
      chosen = "Horse"

      #otherwise set it to a zebra
    else:
      chosen = "Zebra"
    balance -= 0.5

  print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

  if balance < 1:
    play_again = "xxx"
    print("Sorry you have run out of money")
  else:
    play_again = input(" Press Enter to play again "
                      "or 'xxx' to quit")

print()
print("Final_balance ", balance)