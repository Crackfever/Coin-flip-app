#Coin flip app
import random

print("Welcome to the Coin Flip App")
print("I will flip a coin a set number of times.")

#User input
flip_number = int(input("How many times would you like to flip the coin: "))
choice = input("Would you like to see the result of each flip (y/n): ").lower()

print("\nFlipping!!!\n")

#Initialize variables
heads = 0
tails = 0

#The main Loop
for flips in range(flip_number):
  #create the coin object
  coin = random.randint(0,1)

  if coin == 1:
    heads += 1
    if choice.startswith("y"):
      print("HEADS")
  else:
    tails += 1
    if choice,startswith("y"):
      print("TAILS")

  if heads == tails:
    print("At " + str(flips + 1) + " flips, the number of heads and tails were equal at " + str(heads)

