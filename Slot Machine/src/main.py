from src.structure import deposit
from src.play import game


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