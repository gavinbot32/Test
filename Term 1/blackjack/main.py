import card as c
import random
def main():
    eric = c.Hand()
    ryan = c.Hand()
    for i in range(5):
        card = c.Card(random.choice(c.Card.RANK), random.choice(c.Card.SUITS))
        eric.add(card)

    for i in range(5):
        card = c.Card(random.choice(c.Card.RANK), random.choice(c.Card.SUITS))
        ryan.add(card)
    print(eric)
    print("________________________")
    print(ryan)
main()