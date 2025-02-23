import tkinter as tk
import random

def home(root):

    root.title("Blackjack")
    root.geometry("800x600")

    tk.Label(root, text="Blackjack").grid(row=0, column=0)
    tk.Button(root, text="Play", command=play).grid(row=1, column=0)
    tk.Button(root, text="Quit", command=root.quit).grid(row=2, column=0)

def play():

    # Initialize dealer's cards
    dealer_card1 = random.randint(1, 11)
    dealer_card2 = random.randint(1, 11)

    dealer_total = dealer_card1 + dealer_card2

    # Initialize players's cards
    player_card1 = random.randint(1, 11)
    player_card2 = random.randint(1, 11)

    player_total = player_card1 + player_card2

    # Check for initial player Blackjack
    
    if blackjack(player_total):
        pass
    

    # Initial game state
    # print(f"Dealer's Hand: {dealer_card1}, (Hidden)")
    # print(f"Player's Hand: {player_card1}, {player_card2}")

    print(f"Dealer's Hand: {dealer_total}")
    print(f"Player's Hand: {player_total}")

    game_state = True
    while game_state:

        choice = input("Hit or Stand? ")

        if choice == "Hit":

            new_card = hit()
            player_total += new_card



            print("===============================")
            print(f"Dealer's Hand: {dealer_total}")
            print(f"Player's Hand: {player_total}")
            print("===============================")

            if player_bust(player_total):
                game_state = False

            if blackjack(player_total):
                game_state = False
        
        elif choice == "Stand":
            game_state = False

    return
        

        



def player_bust(player_total):
    if player_total > 21:
        print("Player busts!")
        return True


def dealer_bust(dealer_total):
    if dealer_total > 21:
        print("Dealer busts!")

def blackjack(player_total):
    if player_total == 21:
        print("Player wins!")
        return True


def hit():
    new_card = random.randint(1, 11)
    return new_card








def main():

    

    

    root = tk.Tk()
    home(root)
    root.mainloop()

if __name__ == "__main__":
    main()
