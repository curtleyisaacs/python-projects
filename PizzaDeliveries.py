print("Welcome to Pizza Deliveries")
bill = 0
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2

    if extra_cheese == "Y":
        bill += 1

    print(f"Your bill is: R{bill}")


elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3

    if extra_cheese == "Y":
        bill += 1

    print(f"Your bill is: R{bill}")

elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3

    if extra_cheese == "Y":
        bill += 1

    print(f"Your bill is: R{bill}")

else:
    print("You chose the wrong inputs")