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
    cards = ', '.join([f"{card['value']} of {card['suit']}" for card in hand])
    print(f"{name}'s hand: {cards} (Total: {calculate_hand(hand)})")

def blackjack():
    print("\nWelcome to Blackjack!")
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    # Player's Turn
    while True:
        display_hand("Player", player_hand)
        if calculate_hand(player_hand) == 21:
            print("Blackjack! You win!")
            return
        elif calculate_hand(player_hand) > 21:
            print("Bust! You lose.")
            return
        action = input("Do you want to (H)it or (S)tand? ").strip().lower()
        if action == 'h':
            player_hand.append(deck.pop())
        elif action == 's':
            break
    
    # Dealer's Turn
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    display_hand("Dealer", dealer_hand)
    
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)
    
    if dealer_total > 21 or player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins.")
    else:
        print("It's a tie!")

if __name__ == '__main__':
    blackjack()
