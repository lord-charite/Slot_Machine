from src.structure import deposit
from src.play import game


# import rtf

# def create_rtf_file(balance):
#     # Create a new RTF document
#     doc = rtf.Document()

#     # Add text to the document
#     doc.add_text("Slot Machine Game", font_size=24, bold=True)
#     doc.add_paragraph()
#     doc.add_text(f"Current balance is ${balance}", font_size=18)
#     doc.add_paragraph()
#     doc.add_text("Press enter to play (q to quit)", font_size=18)
#     doc.add_paragraph()
#     doc.add_text("Do you want to play again? (y/n)", font_size=18)

#     # Save the document to a file
#     doc.save("slot_machine_game.rtf")
    
def main():
    balance = deposit()
    
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer.lower() == "q":
            break
        balance += game(balance)
    
    print(f"You left with ${balance}")
    #create_rtf_file

def run():
    main()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        run()
    else:
        print("Thanks for playing!")
        



if __name__ == "__main__":
    run()