greeting = "YOU GOT A ZEBRA!"
sides = "Z" * 3

greeting = "{} {} {}".format (sides, greeting, sides)

top_bottom = "Z" * len(greeting)

print(top_bottom)
print(greeting)
print(top_bottom)