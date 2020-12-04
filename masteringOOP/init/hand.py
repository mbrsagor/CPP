class Hand:
    def __init__(self, dealer_card, cards):
        self.dealer_card = dealer_card
        self.cards = cards

    @staticmethod
    def freeze(other):
        hand = Hand(other.dealer_card, other.cards)
        return hand

    @staticmethod
    def split(other, card0, card1):
        hand0 = Hand(other.dealer_card, other.cards[0], )
        hand1 = Hand(other.dealer_card, other.cards[1])
        return hand0, hand1

    def __str__(self):
        return " ".join(map(str, self.cards))
