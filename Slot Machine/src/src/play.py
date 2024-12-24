from src.structure import *

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