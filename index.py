import tkinter as tk
from tkinter import messagebox
import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'suit': suit, 'value': value} for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def calculate_hand(hand):
    total = 0
    aces = 0
    for card in hand:
        if card['value'] in ['Jack', 'Queen', 'King']:
            total += 10
        elif card['value'] == 'Ace':
            aces += 1
            total += 11  # Assume Ace is 11 initially
        else:
            total += int(card['value'])
    
    while total > 21 and aces:
        total -= 10  # Convert Ace from 11 to 1
        aces -= 1
    return total

def display_hand(name, hand):
    for widget in frame.winfo_children():
        widget.destroy()

        for card in hand:
            card_label = tk.Label(frame, text=f"{card['value']} of {card['suit']}")
            card_label.pack()

def check_winner():
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)
    if player_total > 21:
        messagebox.showinfo("Result", "You bust! Dealer wins.")
    elif dealer_total > 21 or player_total > dealer_total:
        messagebox.showinfo("Result", "You win!")
    elif player_total < dealer_total:
        messagebox.showinfo("Result", "Dealer wins.")
    else:
        messagebox.showinfo("Result", "It's a tie!")


def hit():
    if calculate_hand(player_hand) < 21:
     player_hand.append(deck.pop())
    display_hand("Player", player_hand)
    if calculate_hand(player_hand) > 21:
        messagebox.showinfo("Result", "You bust! Dealer wins.")


def stand():
    #prevent repeated execution by disabling buttons
    hit_button.config(state=tk.DISABLED)
    stand_button.config(state=tk.DISABLED)

    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    display_hand("Dealer", dealer_hand)
    check_winner()

def new_game():
    global deck, player_hand, dealer_hand
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    display_hand(plaryer_frame, player_hand)
    display_hand(dealer_frame, dealer_hand)

    #re-enable buttons for new game
    hit_button.config(state=tk.NORMAL)
    stand_button.config(state=tk.NORMAL)

    #GUI setup
window = tk.Tk()

window.title("Blackjack")
window.geometry("400x400")

player_frame = tk.Frame(window)
player_frame.pack(side=tk.LEFT, padx=20, pady=20)

dealer_frame = tk.Frame(window)
dealer_frame.pack(side=tk.RIGHT, padx=20, pady=20)

btn_frame = tk.Frame(window)
btn_frame.pack(side=tk.BOTTOM, pady=20)

hit_button = tk.Button(btn_frame, text="Hit", command=hit)
hit_button.pack(side=tk.LEFT, padx=10)

stand_button = tk.Button(btn_frame, text="Stand", command=stand)
stand_button.pack(side=tk.LEFT, padx=10)

new_game_button = tk.Button(btn_frame, text="New Game", command=new_game)
new_game_button.pack(side=tk.LEFT, padx=10)

# iNITIALIZE GAME
deck = create_deck()
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

display_hand("Player", player_hand)
display_hand("Dealer", dealer_hand)

window.mainloop()

 