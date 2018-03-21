import cards, player
import os

class W_Card(cards.Positionable_Card):
    ACE_VALUE = 14

    @property
    def value(self):
        if self.is_face_up:
            v = W_Card.RANKS.index(self.rank) + 1
        else:
            v = None
        return v


class W_Deck(cards.Deck):
    def populate(self):
        for suit in W_Card.SUITS:
            for rank in W_Card.RANKS:
                self.cards.append(W_Card(rank, suit))

class W_Hand(cards.Hand):
    def __init__(self, name, score = 0):
        super(W_Hand, self).__init__()
        self.name = name
        self.score = score

    def __str__(self):
        # wyswietla liczbe punktow gracza
        rep = self.name + "[" + str(self.score) + "]" + ": "
        rep += super(W_Hand, self).__str__()
        #wyswietla wartosc karty
        if self.total:
            rep += "(" + str(self.total) + ")"

        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        # tworzy wartość karty
        for card in self.cards:
            if card.value == 1:
                t+= W_Card.ACE_VALUE
            else:
                t += card.value

        return t

    # zwieksza liczbe punktow gracza o jeden
    def add_point(self, point):
        self.score += point

class W_Player(W_Hand):
    def lose(self):
        print(self.name, "loses :c")

    def win(self):
        print(self.name, "wins!")

    def push(self):
        print(self.name, "draws.")

class W_Game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = W_Player(name)
            self.players.append(player)

        self.deck = W_Deck()

    def play(self):
        self.deck.populate()
        self.deck.shuffle()

        while len(self.deck.cards) != 0: # gra dopoki sa karty w talii

            # rozdaje po jednej karcie kazdemu z graczy i wyswietla
            self.deck.deal(self.players, per_hand=1)
            for player in self.players:
                print(player)

            # sprawdza kto ma wyzsza karte i dodaje punkty zwyciezcy
            if self.players[0].total > self.players[1].total:
                self.players[0].add_point(1)
            elif self.players[0].total < self.players[1].total:
                self.players[1].add_point(1)
            else:
                # w wypadku remisu wybucha wojna
                print("\nWAR OUTBREAK!!!\n")
                # każdy gracz dostaje kolejna karte, ktora jest odwrocona
                self.deck.deal(self.players, per_hand=1)
                for player in self.players:
                    player.cards[1].flip()
                    print(player)
                # oraz trzecia karte, ktora jest juz wyswietlona normalnie
                self.deck.deal(self.players, per_hand=1)
                for player in self.players:
                    print(player)
                # usuwa dwie pierwsze karty w celu porownania jedynie ostatnich dobranych kart
                    del player.cards[:2]
                # wyswietla ostatnie dobrane karty
                for player in self.players:
                    print(player)

                # sprawdza kto ma wyzsza karte i dodaje punkty zwyciezcy
                if self.players[0].total > self.players[1].total:
                    self.players[0].add_point(3)
                elif self.players[0].total < self.players[1].total:
                    self.players[1].add_point(3)

            # gracz ktory wygral zabiera karty i odklada na osobny stos
            for player in self.players:
                player.clear()

            # koniec tury
            input("Continue... [Enter]\n")

            os.system('cls' if os.name == 'nt' else 'clear')

# po wyczerpaniu sie kart w talii sprawdza kto ma wyzszy wynik i oglasza zwyciezce i przegranego albo remis
        if self.players[0].score > self.players[1].score:
            self.players[0].win()
            self.players[1].lose()
        elif self.players[0].score < self.players[1].score:
            self.players[1].win()
            self.players[0].lose()
        else:
            for player in self.players:
                player.push()

        # usuwa wszystkie karty
        for player in self.players:
            player.clear()
            player.score = 0


def intro(names):
    with open("intro.txt", "r") as intro_file:
        header = intro_file.readline()
        body = intro_file.read()

        print(header)
        print("Hello", names[0],"and", names[1], "!", sep=' ')
        print(body)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("intro.txt", "r") as intro_file:
        header = intro_file.readline()
        body = intro_file.read()

    names = []
    for i in range(2):
        name = input("Name of the player nr {}: ".format(i+1))
        names.append(name)
    os.system('cls' if os.name == 'nt' else 'clear')

    intro(names)

    input("\nPress Enter to begin!")
    os.system('cls' if os.name == 'nt' else 'clear')

    game = W_Game(names)

    again = None
    while again != "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        game.play()
        again = player.ask_yes_no("Do you wanna play again? (Y/N): ")

main()
