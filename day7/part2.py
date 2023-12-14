from helper import *

cards = readData("case1.txt")
cards = [NewCardHand(card[0], card[1]) for card in cards]

cards = sorted(cards, key=lambda card: card.priority)

winnings = 0
for idx, card in enumerate(cards):
    winnings += card.bid * (idx + 1)

print(winnings)