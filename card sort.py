cards = [
    "jack of diamonds",
    "three of clubs",
    "ace of hearts",
    "10 of spades",
    "king of clubs",
]

# Lower number means earlier in the sorted order
value_order = {
    "ace": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "10": 10,
    "jack": 11,
    "queen": 12,
    "king": 13,
}

suit_order = {
    "clubs": 1,
    "diamonds": 2,
    "hearts": 3,
    "spades": 4,
}


def card_key(card):
    value, _, suit = card.partition(" of ")
    return value_order[value.lower()], suit_order[suit.lower()]


swaps = 0

# Insertion sort, based on the starter code
for index in range(1, len(cards)):
    current_card = cards[index]
    position = index

    while (
        position > 0
        and card_key(cards[position - 1]) > card_key(current_card)
    ):
        cards[position] = cards[position - 1]
        position -= 1
        swaps += 1

    cards[position] = current_card

print("Sorted cards:")
for card in cards:
    print(card)

print("Number of swaps:", swaps)