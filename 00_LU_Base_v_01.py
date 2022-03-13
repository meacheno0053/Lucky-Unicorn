
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
  print("the rules of the game go here")
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
played_before = yes_no("have you played before? ")

if played_before == "no":
  instructions()

# print("program continues")

how_much = num_check ("how much would you like to play with? " , 0, 10 )

print("you will be spending${}".format (how_much))