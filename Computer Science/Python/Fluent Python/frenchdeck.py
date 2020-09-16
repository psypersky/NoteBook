import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in list(range(2, 11)) + list('JQKA')]
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # we consider position 0 the top of the deck
        self.__cards = [Card(rank, suit)
                      for suit in self.suits for rank in self.ranks]

    # standard python operation, following the python data model
    def __len__(self):
        return len(self.__cards)

    # dunder-getitem
    def __getitem__(self, position):
        return self.__cards[position]


print('creating deck')
deck = FrenchDeck()

## Loop through deck
# for n in deck: # for card in reversed(deck)
#     print(n)

# print('len: ' + str(len(deck)))

## Select random card
# print('random card:')
# print(choice(deck))

# print(deck[:3])
# print(deck[12::13])

# print(Card('Q', 'hearts') in deck)

# List deck in order of increasing rank
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
print(suit_values)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)