import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in list(range(2, 11)) + list('JQKA')]
    suits = 'spades diamons clubs hearts'.split()

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

for n in deck: # for card in reversed(deck)
    print(n)

print('len: ' + str(len(deck)))

print('random card:')
print(choice(deck))

print(deck[:3])
print(deck[12::13])

print(Card('Q', 'hearts') in deck)