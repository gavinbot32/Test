import card as c
import hands as h
from commonGameFunctions import *
class Bj_Card(c.Pos_card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.isfaceup:
            v = Bj_Card.RANK.index(self.rank)+1
            if v > 10:
                v=10
        else:
            v=None
        return v
class Bj_Hand(h.Hand):

    def __init__(self,name):
        super(Bj_Hand, self).__init__()
        self.name = name

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        #adds up card values, treats each Ace as 1
        t = 0
        for card in self.cards:
            t+=card.value
        #determine if hand contains ace
        contains_ace = False
        for card in self.cards:
            if card.value == Bj_Card.ACE_VALUE:
                contains_ace = True
        if contains_ace and t <=11:
            t+=10
        return t

    def is_busted(self):
        return self.total>21

    def __str__(self):
        rep = h.Hand.__str__(self)
        rep +=self.name+"\t"+"("+str(self.total)+")"
        return rep
class Bj_Player(Bj_Hand):

    def is_hitting(self):
        response = askYorN("\n"+self.name+",do you want a hit? (Y/N: ")
        return response == "y"

    def lose(self):
        print(self.name, "you lost")
    def win(self):
        print(self.name, "you won")
    def pushed(self):
        print(self.name, "you pushed")
    def bust(self):
        print(self.name, "you bust")
        self.lose()
    def fliphand(self):
        for card in self.cards:
            card.flip()
class Bj_Dealer(Bj_Hand):
    def is_hitting(self):
        soft = True
        for card in self.cards:
            if card.value >= 10:
                soft = False
        if self.total < 17 or (self.total == 17 and soft):
            return True
        else:
            return False
    def bust(self):
        print(self.name, "busts.")
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
class Bj_Game(object):
    pass

