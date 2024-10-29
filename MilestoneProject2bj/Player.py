from Card import Card

class Player():

    def __init__(self, name, balance = 100):
        self.name  = name
        self.cards = []
        self.balance = balance
   
    def add_cards(self, cards):
        if type(cards) == type([]):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)

    def clear_hand(self):
        self.cards = []

    def __str__(self):
        return f'{self.name} has \t{len(self.cards)} cards.'
    
    def print_hand(self, isFirstCardHidden=True):

        dealer_cards = ''
        if (isFirstCardHidden):
            dealer_cards += f'??\t'
        else:
            dealer_cards += f'{self.calculate_hand_score()}\t'
        

        if (isFirstCardHidden):
            dealer_cards += f' {Card.BackOfCard}'
        else:
            dealer_cards += f'{self.cards[0]}'

        for card in self.cards[1:]:
            dealer_cards += f' {card}'

        return dealer_cards
    #############################################

    def calculate_hand_score(self):

        number_of_aces = 0
        score          = 0

        for card in self.cards:
            if (card.rank == 'A'):
                number_of_aces += 1
            
            score += card.values[card.rank]

        while(score > 21 and number_of_aces > 0):
            number_of_aces -= 1
            score          -= 10

        return score


        

    