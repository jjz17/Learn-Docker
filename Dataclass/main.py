from dataclasses import dataclass, field
from typing import List, Iterable

@dataclass
class Position:
    name: str
    lat: float = 0.0
    lon: float = 0.0

@dataclass
class ComplexPosition:
    name: str
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})

@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self) -> str:
        return f'{self.rank}{self.suit}'

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        # !s in the f string calls the __str__ method for the PlayingCard
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


print(PlayingCard(rank='A', suit='♠'))
print(Deck())