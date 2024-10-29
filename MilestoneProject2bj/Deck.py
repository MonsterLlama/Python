from Card import Card
from random import shuffle

class Deck():

    def __init__(self):
        self.deck = self.create()
        self.shuffle()

    def __str__(self): 
        output = 'Cards: '       
        for card in self.deck:
            output += f' [{card}]'       
        return output

    def create(self):
        self.deck = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.deck.append(Card(suit, rank))
        return self.deck

    def shuffle(self):
        if len(self.deck) > 1:
            shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            return None