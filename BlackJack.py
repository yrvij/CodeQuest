# BlackJack Game Code:

# Step 1: Imports and Global Variables -
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,
         'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing = True

# Step 2: Card class -# Step 2 
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return self.rank + ' of ' + self.suit

# Step 3: Deck class -
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    

# Step 4: Hand Class - # Step 4 
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
            
# Step 5: Chips Class -
class Chips:
    def __init__(self,total = 100):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

# Step 6: Taking bets -
def take_bet(chips):
    while True:
        try: 
            chips.bet = int(input('How many chips would you like to bet?: '))
        except ValueError:
            print('Sorry, please input an integer: ')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips. You only have: {chips.total}')
            else:
                break
                
# Step 7: Taking hits -
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    
# Step 8: Hit or Stand? -
def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input('Hit or Stand?: Enter h or s.')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands - Dealer's turn")
            playing = False
        else:
            print('Sorry, I did not understand that. Please enter h or s only.')
            continue
            
        break
        
# Step 9: Display cards -
def show_some(player,dealer):
    print("DEALER'S HAND:")
    print('one card hidden!')
    print(dealer.cards[1])
    print('\n')
    print('\n')
    print("PLAYER'S HAND:")
    for card in player.cards:
        print(card)
    print('\n')
    print('\n')

def show_all(player,dealer):
    print("DEALER'S HAND:")
    for card in dealer.cards:
        print(card)
    print('\n')
    print('\n')
    print("PLAYER'S HAND:")
    for card in player.cards:
        print(card)
    print('\n')
    print('\n')
    
# Step 10: End-of-game-scenarios -
def player_busts(player,dealer,chips):
    print('BUST PLAYER!')
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print('PLAYER WINS!')
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print('DEALER WINS!')
    chips.lose_bet()
def push():
    print('Dealer and player tie! PUSH')

# Step 11: Game Logic -
while True:
    # Print opening statement:
    
    print('Welcome to BlackJack!')
    
    # Create + shuffle deck + deal two cards to each player:
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the player's chips:
    player_chips = Chips()
    
    # Prompt player for bet:
    take_bet(player_chips)
    
    # Show cards (keep one dealer card hidden):
    show_some(player_hand,dealer_hand)
    
    while playing:
        # Prompt for player to hit or stand:
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden):
        show_some(player_hand,dealer_hand)
        
        # If player_hand > 21, run player_busts() and break out of loop:
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
            
        # If player hasn't busted, player dealer's hand:
        if player_hand.value <= 21:
            while dealer_hand.value < player_hand.value:
                hit(deck,dealer_hand)
            
            # Show all cards:
            show_all(player_hand,dealer_hand)
            
            # Run different winning scenarios:
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)
        
        # Inform player of chip total:
        print(f"\n Player's total chips are at: {player_chips.total}")
        
    # Ask to play again:
    new_game = input('Would you like to play again?: y/n ')
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing BlackJack!')
        break
