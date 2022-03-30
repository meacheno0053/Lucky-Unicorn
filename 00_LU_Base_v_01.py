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
      print("Please answer: yes / no")

   


def instructions ():
  print("**** How to Play: ****")
  print()
  print("""Choose a starting amount (minimum $1, maximum $10). 

Then press <Enter> to play. You will get either a horse, a zebra, a donkey or a unicorn.  It costs $1 per round. Depending on your prize you might win some of the money back. Here's the payout amounts:
  Unicorn: $5.00 (balance increases by $4)
  Horse: $0.50 (balance decreases by $0.50)	
  Zebra: $0.50 (balance decreases by $0.50)
  Donkey $0.00 (balance decreases by $1.00)

Can you avoid the donkeys, get the unicorns and walking home with the money??

Hint: to quit while you are ahead, type 'xxx' instead of pressing <Enter>""")
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
      


def statement_generator(statement, decoration, style):

  sides = decoration * 2

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  if style == 3:
  
    print(top_bottom)
    print(statement)
    print(top_bottom)
  else:
    print(statement)

  return ""

# ******* Main routine starts here ******

statement_generator("** Welcome to the Lucky Unicorn Game **", "*", 3)

print()
played_before = yes_no(" ?? Have you played before: ??" )
print()

if played_before == "no":
  instructions()

print()

# print("program continues")

how_much = num_check (" ++ How much would you like to play with?: ++" , 0, 10 )

print(" -- You will be spending ${} -- ".format (how_much))

balance = how_much

rounds_played = 0

play_again = ""
while play_again == "":

  # play_again = input ("press <Enter> to play...").lower()

    #increase # of rounds played
  rounds_played += 1

  # print round number
  print()
  rounds_heading = "*** Round #{} ***".format(rounds_played)
  statement_generator(rounds_heading, "*", 1)
  print()
  
  chosen_num = random.randint (1, 100)
  
  # Adjust balance
  # if the random # is between 1 and 5,
  # user gets a unicorn (add $4 to balance)
  if 1 <= chosen_num <= 5:
    chosen = "Unicorn"
    prize_decoration = "!"
    balance += 4
    
    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
  elif 6 <= chosen_num <= 36:
    chosen = "Donkey"
    prize_decoration = "D"
    balance -= 1

    # the token is either horse or zebra
    # in both cases, subtract $0.50 from the balance
  else:
    if chosen_num % 2 ==0:
      chosen = "Horse"
      prize_decoration = "H"

      #otherwise set it to a zebra
    else:
      chosen = "Zebra"
      balance -= 0.5
      prize_decoration = "Z"
    
  feedback = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)

  statement_generator(feedback, prize_decoration, 1)

  if balance < 1:
    play_again = "xxx"
    print("Sorry you have run out of money")
  else:
    play_again = input(" Press Enter to play again "
                      "or 'xxx' to quit")

print()
print("Final_balance: $", balance)
