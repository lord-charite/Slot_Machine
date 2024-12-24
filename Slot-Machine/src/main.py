def deposit():
    while True: # continue prompting until a valid amout is entered
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): # checking if the input is a number
            amount = int(amount)
            if amount > 0:
                break #break out of the loop
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please input a number.")
    return amount