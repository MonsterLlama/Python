from Deck   import Deck
from Card   import Card
from Player import Player
from os     import system
from time   import sleep

class Game():

    def __init__(self):
        self.player1 = Player('Dealer')
        self.player2 = Player('Player')

        # Create new Deck (pre-shuffled)
        self.deck = Deck()

    def __str__(self):
        pass

    def game_on(self):

        still_playing = True        
        while(still_playing):
            # New deck for each hand and clear hands
            self.deck = Deck()
            self.player1.clear_hand()
            self.player2.clear_hand()

            # Validate player has money to bet
            if (self.player2.balance <= 0):
                print('You have run out of money!')
                print('Game Over!')
                exit()

            # Ask Player how much to bet
            bet = 0
            while (bet <= 0 and self.player2.balance >= bet):
                try:
                    bet = int(input(f'Input bet amount from $1 to ${self.player2.balance}: '))
                    if (bet > self.player2.balance):                  
                        system('cls')
                        print('Invalid bet amount, please try again!')
                        input('Press any key to continue..')
                        bet = 0
                except:
                    system('cls')
                    print('Invalid bet amount, please try again!')
                    input('Press any key to continue..')
                    bet = 0
                
            self.player2.balance -= bet

            # Deal two cards to dealer
            self.player1.cards.append(self.deck.deal_card())
            self.player1.cards.append(self.deck.deal_card())

            # Deal two cards to player
            self.player2.cards.append(self.deck.deal_card())
            self.player2.cards.append(self.deck.deal_card())

            player1_score = self.player1.calculate_hand_score()
            player2_score = self.player2.calculate_hand_score()

            # Player's Turn
            is_player_turn_active = True
            while(is_player_turn_active):
                self.print_table()
                # Ask player for hit or stay
                play_action = input('Do you want to "H"it or "S"tay? ')
                
                if (play_action.upper() in ['H', 'S']):
                    if (play_action.upper() == 'H'):
                        self.player2.cards.append(self.deck.deal_card())
                        player2_score = self.player2.calculate_hand_score()
                        if (player2_score > 21):
                            # player has busted
                            is_player_turn_active = False
                            break
                    else:
                        is_player_turn_active = False
            # end while

            self.print_table()

            # Dealer's Turn
            # Dealer's Strategy: Hit 'til over players hand if player hasn't busted.

            # check if Dealer has already won:
            if (player2_score > 21):
                self.print_table(showDealersFirstCard=True)
                print(f'{self.player2.name} has busted and loses ${bet}!')
                if (self.player2.balance <= 0):
                    # player has run out of money!
                    still_playing = False
                input('Press any key to continue..')
                continue

            while(player1_score < player2_score and player1_score < 21):
                # Dealer draws a card        
                self.player1.cards.append(self.deck.deal_card())
                player1_score = self.player1.calculate_hand_score()
          
            if (player1_score == 21 and player2_score == 21):
                # Tie
                # Return bet to player
                self.player2.balance += bet # return bet
                self.print_table(showDealersFirstCard=True)
                input('Press any key to continue..')

            elif(player1_score > 21):
                # Dealer busted!
                self.player2.balance += (bet * 2)   # return bet + winnings
                self.print_table(showDealersFirstCard=True)
                print(f'{self.player1.name} has busted! {self.player2.name} wins ${bet}!')
                input('Press any key to continue..')
            else:
                # Dealer wins!
                self.print_table(showDealersFirstCard=True)
                print(f'{self.player1.name} wins hand: {player1_score} to {player2_score}.')
                if (self.player2.balance <= 0):
                    # player has run out of money!
                    still_playing = False
                    input('Press any key to continue..')
                    continue


    def print_table(self, showDealersFirstCard = False):
        system('cls')
        print(f'Python Black Jack (c) 2024 - MonsterLlama')
        print()
        print(f'Balance: ${self.player2.balance}')
        print()
        print(f'{self.player1.name} score:\t{self.player1.print_hand(isFirstCardHidden=not showDealersFirstCard)}')
        print(f'{self.player2.name} score:\t{self.player2.print_hand(isFirstCardHidden=False)}')
        print()