while True:
    print(f"Welcome to the Tip Calculator")

    bill = float(input("What is your bill? R"))
    tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
    people = int(input("How many people to split the bill? "))

    if tip == 10:
        total = bill * 1.1 / people
        print(f"Each person should pay: R{round(total,2)}")
        break
    elif tip == 12:
        total = bill * 1.12 / people
        print(f"Each person should pay: R{round(total,2)}")
        break
    elif tip == 15:
        total = bill * 1.15 / people
        print(f"Each person should pay: R{round(total,2)}")
        break
    else:
        print(f"Enter selected amount")

