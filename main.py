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
        # display a number of a player's points
        rep = self.name + "[" + str(self.score) + "]" + ": "
        rep += super(W_Hand, self).__str__()
        # display card value
        if self.total:
            rep += "(" + str(self.total) + ")"

        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        # create card value
        for card in self.cards:
            if card.value == 1:
                t+= W_Card.ACE_VALUE
            else:
                t += card.value

        return t

    # increment number of player's points
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

        while len(self.deck.cards) != 0: # loop until there're cards in the deck

            # pass to every player one card and display them
            self.deck.deal(self.players, per_hand=1)
            for player in self.players:
                print(player)

            # check who has higher card and gives the winner points
            if self.players[0].total > self.players[1].total:
                self.players[0].add_point(1)
            elif self.players[0].total < self.players[1].total:
                self.players[1].add_point(1)
            else:
                # im case of draw there is a war outbreak
                print("\nWAR OUTBREAK!!!\n")
                # every player gets additional card which is flipped
                self.deck.deal(self.players, per_hand=1)
                for player in self.players:
                    player.cards[1].flip()
                    print(player)
                # and then a third card which is displayed normally
                self.deck.deal(self.players, per_hand=1)
                for player in self.players:
                    print(player)
                # remove two initial cards in order to compare only the latest
                    del player.cards[:2]
                # display freshly taken cards
                for player in self.players:
                    print(player)

                # check who has higher card and gives the winner points
                if self.players[0].total > self.players[1].total:
                    self.players[0].add_point(3)
                elif self.players[0].total < self.players[1].total:
                    self.players[1].add_point(3)

            # a winner takes cards and put them away to a seperated stack
            for player in self.players:
                player.clear()

            # end of a turn
            input("Continue... [Enter]\n")

            os.system('cls' if os.name == 'nt' else 'clear')

# when the deck is empty, check who has higher score and declare the winner and the looser of the game or draw
        if self.players[0].score > self.players[1].score:
            self.players[0].win()
            self.players[1].lose()
        elif self.players[0].score < self.players[1].score:
            self.players[1].win()
            self.players[0].lose()
        else:
            for player in self.players:
                player.push()

        # delete all cards
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
