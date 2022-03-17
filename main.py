import random

def greet(massage):
    print(massage)

greet("Hello in my dice roller project")

def dice(massage2):
    print(massage2)

dice("You can use this dice : 4, 6, 8, 10, 12, 20, 100")

x = int(input("Choose which dice do you want to roll?:"))

def rolling_one_dice():
    while True:
        print("Rolling the dice.....")
        print(random.randint(1, x))
        choice = str(input("Do you want to roll again? Y/N:"))
        if choice.lower() == "n":
            print("Thx for testing :) ")
            break
print(rolling_one_dice())
"""
z = int(input("How many dice you rolling?:"))

def rolling_more_dice(x, z):
    while True:
        print("Rolling the dice.....")
        print(random.randint(1,x))
        more = str(input("How many dice you rolling? Y/N:"))
        if more.lower() == "y":
            print(random.randint(1,z))
        else:
            print(x * z)


print(rolling_more_dice)



while True:
    print("Rolling the dice")
    print(random.randint(1,x))
    choice = str(input("Do you want to roll again? Y/N:"))
    if choice.lower() == "n":
        print("Thx for testing :) ")
        break

"""

