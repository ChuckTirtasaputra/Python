import random

def create_deck():
    suits = ["♥", "♦", "♣", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [rank + suit for suit in suits for rank in ranks]
    return deck

def deal_card(deck):
    return deck.pop()

def calc_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        rank = card[:-1]
        if rank.isdigit():
            value += int(rank)
        elif rank in ("J", "Q", "K"):
            value += 10
        elif rank == "A":
            value += 11
            ace_count += 1
    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1
    return value

def display_hand(hand, hide_first_card=False):
    if hide_first_card:
        print("[Hidden]", end=" ")
        for card in hand[1:]:
            print(card, end=" ")
    else:
        for card in hand:
            print(card, end=" ")
    print()

def play_blackjack():
    deck = create_deck()
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    for _ in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))

    print("Dealer's hand:", end=" ")
    display_hand(dealer_hand, hide_first_card=True)
    print("Your hand:", end=" ")
    display_hand(player_hand)

    while True:
        player_value = calc_hand_value(player_hand)
        if player_value == 21:
            print("Blackjack!")
            break
        elif player_value > 21:
            print("Bust!")
            break

        action = input("Hit or stand? (h/s): ")
        if action.lower() == "h":
            player_hand.append(deal_card(deck))
            print("Your hand:", end=" ")
            display_hand(player_hand)
        elif action.lower() == "s":
            break
        else:
            print("Invalid input.")

    print("Dealer's hand:", end=" ")
    display_hand(dealer_hand)
    dealer_value = calc_hand_value(dealer_hand)
    print("Dealer's value:", dealer_value)

    if player_value > 21:
        print("Dealer wins!")
    elif dealer_value > 21:
        print("You win!")
    elif dealer_value >= player_value:
         print("Dealer wins!")
    elif player_value > dealer_value:
        print("You win!")

play_blackjack()
