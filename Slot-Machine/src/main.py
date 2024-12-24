import random

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# gloabal variables
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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


def get_number_of_lines():
    while True: # continue prompting until a valid amout is entered
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): # checking if the input is a number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break #break out of the loop
            else:
                print(f"Enter a valid number of lines (1-{MAX_LINES})")
        else:
            print("Please input a number.")
    return lines

def get_bet():
    while True: # continue prompting until a valid amout is entered
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): # checking if the input is a number
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break #break out of the loop
            else:
                print("Amount must be greater than between $" + str(MIN_BET) + " and $" + str(MAX_BET) + ".")
        else:
            print("Please input a number.")
    return amount
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Ready to play?")
    
    
    
main()