
def yes_no (question):
  valid = False
  while not valid:
    response = input(question).lower()
    
    if response == "yes" or response == "y": 
      print("you chose yes")
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
      
# Main Routine goes here
played_before = yes_no("have you played before?")

if played_before == "no":
  instructions()

print("program continues")
