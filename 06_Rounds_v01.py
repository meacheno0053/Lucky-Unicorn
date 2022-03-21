# set balance for testing purpose
balance = 5

rounds_played = 0

play_again = input ("press <Enter> to play...")
while play_again == "":

    #increase # of rounds played
  rounds_played += 1

  # print round number
  print(rounds_played)
  balance -= 1 
  print("balance: ", balance)
  print()
  
  play_again = input ("press enter to play again " 
                     "or 'xxx' to quit")

print()
print("final_balance", balance)