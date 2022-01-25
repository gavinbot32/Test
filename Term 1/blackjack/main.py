import card as c
import random
def main():
    rank = random.choice(c.Card.RANK)
    suit = random.choice(c.Card.SUITS)
    gavin = c.Pos_card(rank,suit)
    print(gavin)
    input("press enter to flip")
    gavin.flip()
    print(gavin)

main()