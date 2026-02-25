from playingcard import PlayingCard, CardSuit, _valid_rank_, _convert_to_rank
from collections.abc import Container
import unittest
import random


_full_deck_ = [PlayingCard(s, r) for s in CardSuit for r in range(1, 14)]


class DirtyDeck(Container):

    def __init__(self, *, hide=None):
        self.deck = _full_deck_.copy()
        self.hidden = None
        if hide is not None:
            if not _valid_rank_(hide):
                raise ValueError(f"{hide} is not a card rank")
            self.hidden = _convert_to_rank(hide)

    def __str__(self):
        retstr = ""
        for c in self.deck:
            retstr += f"{str(c)} "
        return retstr

    def __contains__(self, c):
        return c in self.deck

    def __len__(self):
        return len(self.deck)

    def __iter__(self):
        return iter(self.deck)

    def shuffle(self):
        self.deck = _full_deck_.copy()
        length = len(self.deck)

        for x in range(length - 1, 0, -1):
            y = random.randint(0, x)
            self.deck[x], self.deck[y] = self.deck[y], self.deck[x]

        if self.hidden is not None:
            topCard = [x for x in self.deck if x.rank != self.hidden]
            botCard = [x for x in self.deck if x.rank == self.hidden]
            self.deck = topCard + botCard
        

    def deal(self):
        if not self.deck:
            raise IndexError("Deck is Empty")
        
        card = self.deck.pop(0)

        if len(self.deck) <= (_full_deck_) // 4:
            raise ResourceWarning("low deck")
        
        return card


if __name__ == "__main__":

    d = DirtyDeck()  # rework as unittests
    print(d)
    print(f"len={len(d)}")

    for rank in [10, "Jack", "Queen", "King", "Ace", "Joker", 2]:
        _ = DirtyDeck(hide=rank)

    try:
        _ = DirtyDeck(hide=15)
    except Exception:
        print("invalid hide fails")
