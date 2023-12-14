from collections import Counter

HAND_PRIORITY = {
    "Five of a kind": 7,
    "Four of a kind": 6,
    "Full house": 5,
    "Three of a kind": 4,
    "Two pair": 3,
    "One pair": 2,
    "High card": 1
}

CARD_PRIORITY = {
    'A': '13', 'K': '12', 'Q': '11', 'J': '10', 'T': '09', '9': '08', '8': '07',
    '7': '06', '6': '05', '5': '04', '4': '03', '3': '02', '2': '01'
}

NEW_CARD_PRIORITY = {
    'A': '13', 'K': '12', 'Q': '11', 'T': '10', '9': '09', '8': '08', '7': '07',
    '6': '06', '5': '05', '4': '04', '3': '03', '2': '02', 'J': '01'
}

class CardHand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.priority = [None, None]

        self.prioritize()

    def prioritize(self):
        count = Counter(self.cards)
        if len(count) == 1:
            self.priority[0] = HAND_PRIORITY["Five of a kind"]
        elif 4 in count.values():
            self.priority[0] = HAND_PRIORITY["Four of a kind"]
        elif 3 in count.values() and 2 in count.values():
            self.priority[0] = HAND_PRIORITY["Full house"]
        elif 3 in count.values():
            self.priority[0] = HAND_PRIORITY["Three of a kind"]
        elif len(count) == 3 and 2 in count.values():
            self.priority[0] = HAND_PRIORITY["Two pair"]
        elif 2 in count.values():
            self.priority[0] = HAND_PRIORITY["One pair"]
        elif len(count) == 5:
            self.priority[0] = HAND_PRIORITY["High card"]

        pr = [CARD_PRIORITY[c] for c in self.cards]
        pr = int(''.join(pr))

        self.priority[1] = pr

    def __repr__(self):
        return self.cards

class NewCardHand(CardHand):
    def prioritize(self):
        count = Counter(self.cards)
        pr = [NEW_CARD_PRIORITY[c] for c in self.cards]
        pr = int(''.join(pr))

        self.priority[1] = pr

        if 'J' in count and len(count) > 1:
            j_count = count.pop('J')
            max_key = max(count, key=count.get)
            count[max_key] += j_count
        
        if len(count) == 1:
            self.priority[0] = HAND_PRIORITY["Five of a kind"]
        elif 4 in count.values():
            self.priority[0] = HAND_PRIORITY["Four of a kind"]
        elif 3 in count.values() and 2 in count.values():
            self.priority[0] = HAND_PRIORITY["Full house"]
        elif 3 in count.values():
            self.priority[0] = HAND_PRIORITY["Three of a kind"]
        elif len(count) == 3 and 2 in count.values():
            self.priority[0] = HAND_PRIORITY["Two pair"]
        elif 2 in count.values():
            self.priority[0] = HAND_PRIORITY["One pair"]
        elif len(count) == 5:
            self.priority[0] = HAND_PRIORITY["High card"]

def readData(path):
    data = []
    with open(path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            card, bid = line.split()
            data.append((card, int(bid)))

    return data

if __name__ == "__main__":
    print(readData("test-case1.txt"))