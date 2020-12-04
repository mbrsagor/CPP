"""
class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()


class CardNumber(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


if __name__ == '__main__':
    card_number = CardNumber(40, 90)
    print(card_number._points())


class AceCard(Card):
    def _points(self):
        return 1, 11


class FaceCard(Card):
    def _points(self):
        return 10, 10
"""


class Card:
    pass


class CardNumber(Card):
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft


class NumberCard(Card):
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = "A"
        self.hard, self.soft = 1, 11
        super().__init__(str(rank), suit, rank, rank)


class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__("A", suit, 1, 11)


class FaceCard(Card):
    def __init__(self, rank, suit):
        super().__init__({11: 'J', 12: 'Q', 13: 'K'}[rank], suit, 10, 10)
