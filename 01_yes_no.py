# Ask the user if they have played before
show_instructions = input("have you played before?").lower()

# If they say yes, output 'program continues'
if show_instructions == "yes":
  print("program continues")

elif show_instructions == "y":
  print("program continues")

elif show_instructions == "no":
  print("display instructions")

elif show_instructions == "n" :
  print("display instructions")
  
  # If they say no, output 'display instructions'
else:
  print("Please answer yes / no") 

print("you chose {}".format(show_instructions))