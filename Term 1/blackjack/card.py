class Card(object):

    RANK = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["♣","♦","♥","♠"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = str.format("""
            ______________
            |{0}{1}          |
            |            |
            |            |
            |            |
            |            |
            |            |
            |            |
            |          {1}{0}|
            ______________
            
            
            
            """,self.rank,self.suit)

        return rep

    def flip(self):
        self.faceUp =  not self.faceUp

class Pos_card(Card):
    def __init__(self,rank,suit):
        super(Pos_card, self).__init__(rank,suit)
        self.faceUp = False

    def __str__(self):
        if self.faceUp:
            rep = str.format("""
                        ______________
                        |{0}{1}          |
                        |            |
                        |            |
                        |            |
                        |            |
                        |            |
                        |            |
                        |          {1}{0}|
                        ______________



                        """, self.rank, self.suit)
        else:
            rep = str.format("""
                       ______________
                       |            |
                       |            |
                       |            |
                       |            |
                       |            |
                       |            |
                       |            |
                       |            |
                       ______________



                       """)
        return rep

class Hand(object):

    def __init__(self):
        self.cards = []

    @property
    def cards_total(self):
        return len(self.cards)

    def __str__(self):
        rep=""
        if self.cards:
            for card in self.cards:
                rep+=str(card)
        else:
            rep = "<EMPTY>"

        return rep
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def clear(self):
        self.cards.clear()

