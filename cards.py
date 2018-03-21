import csv


class Card:
    """ Game card. """
    # import RANKS and SUITS from external .csv file
    RANKS = []
    SUITS =[]

    with open("ranks_suits.csv") as ranks_suits_file:
        reader = csv.reader(ranks_suits_file)
        rank_suits_list = list(reader)

    for value in rank_suits_list:
        RANKS.append(value[0])
        if value[1] != '': # columns are not equal, so it's necessary to do not assign empty strings to SUITS
            SUITS.append(value[1])


    def __init__(self, rank="", suit=""):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        rep = ""
        if self.cards:
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    # clear
    def clear(self):
        self.cards = []

    # add
    def add(self, card):
        self.cards.append(card)

    # give another player
    def give(self, card, otherHand):
        self.cards.remove(card)
        otherHand.add(card)


class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("I cannot deal. There's not enough cards.")


class Unprintable_Card(Card):
    def __str__(self):
        return "<latent card>"


class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up=True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "🂠"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up
