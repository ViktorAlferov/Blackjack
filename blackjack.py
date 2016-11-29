# Blackjack

import cards, player 

class Bjack_Card(cards.Card):
    """ A Blackjack Card. """
    ACE_VALUE = 1

    @property 
    def value(self):
        if self.nominal:
            v = Bjack_Card.NOMINAL.index(self.nominal) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class Bjack_Deck(cards.Deck):
    """ A Blackjack Deck. """
    def home(self):
        for suit in Bjack_Card.SUITS: 
            for nominal in Bjack_Card.NOMINAL: 
                self.cards.append(Bjack_Card(nominal, suit))
    

class Bjack_Hand(cards.Hand):
    """ A Blackjack Hand. """ 
    def __init__(self, name):
        super(Bjack_Hand, self).__init__()
        self.name = name

    def __str__(self):
        bh = self.name + ":\t" + super(Bjack_Hand, self).__str__()  
        if self.total:
            bh += "(" + str(self.total) + ")"        
        return bh

    @property     
    def total(self):
    
        t = 0
        for card in self.cards:
              t += card.value
        contains_ace = False
        for card in self.cards:
            if card.value == Bjack_Card.ACE_VALUE:
                contains_ace = True
        if contains_ace and t <= 11:
            
            t += 10   
                
        return t

    def is_busted(self):
        return self.total > 21


class Bjack_Player(Bjack_Hand):
    """ A Blackjack Player. """
    def is_hitting(self):
        response = player.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def push(self):
        print(self.name, "pushes.")



        
class Bjack_Dealer(Bjack_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")






class Bjack_Game(object):
    """ A Blackjack Game. """
    def __init__(self, names, player_wins=0, diler_wins=0):
        self.player_wins = player_wins
        self.diler_wins = diler_wins      
        self.players = []
        for name in names:
            player = Bjack_Player(name)
            self.players.append(player)

        self.dealer = Bjack_Dealer("Dealer")

        self.deck = Bjack_Deck()
        self.deck.home()
        self.deck.shuffle()


    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()


    def play(self):        
        self.deck.deal([self.dealer] + self.players, per_hand = 2)
        for player in self.players:
            print(player)
        for player in self.players:
            self.__additional_cards(player)
        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                	player.win()                    
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                    	player.win()
                    elif player.total < self.dealer.total:
                    	self.diler_wins += 1
                    	player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear_card()
        self.dealer.clear_card()


def main():
    print("\t\tBlackjack!\n")
    names = []
    number = player.ask_number("How many players? (1 - 5): ", low = 1, high = 6)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()
        
    game = Bjack_Game(names)
    again = None
    while again != "n":
        game.play()      
        again = player.ask_yes_no("\nDo you want to play again?: ")


main()
input("\n\nPress the enter key to exit.")
