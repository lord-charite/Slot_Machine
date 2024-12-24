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


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]   # all symbols in the same column must be the same
            if symbol != symbol_to_check:
                break   
        else: # else run if no break in the for loop
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winning_lines, winnings
        
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #gives us key and value
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [] #nested list
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #copy of all_symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) #copy was necessary because we need to preserve for next column iteration
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    
    #transposing the matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1: #check not last column, style choice for "|""
                print(column[row], end=" | ") # end tells the print function not to go to the next line
            else:
                print(column[row], end="")

        print()

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

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    
    print_slot_machine(slots)
    
    winning_lines, winnings = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines) # * unpacks the list
    
    return winnings - total_bet #how much lost and gained

def main():
    balance = deposit()
    
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += game(balance)
    
    print(f"You left with ${balance}")
main()