from deckofcards import Deck,Card

class Boot(Deck):
    def __init__(self,numberofdecks=1):
        # make sure numberofdecks is valid 
        if type(numberofdecks) is not int or numberofdecks < 1:
            raise ValueError("numberofdecks argument must be a positive integer. The current value is: {}".format(numberofdecks))
        self.numberofdecks = numberofdecks
        self.loadnewboot()
        self.shuffledeck()

    def loadnewboot(self):
        self.loadnewdeck()
        self.deck  *= self.numberofdecks
        # use inherited loadnewdeck() method to load 1 deck
        # then increase number of decks in Boot to numberofdecks

class Player:
    def __init__(self,name=None,dealer=False):
        # argument error checking
        if type(dealer) is not bool:
            raise ValueError("dealer argument must be a boolean. The current value is: {}".format(dealer))
        if type(name) is not str and name is not None:
            raise ValueError("player name must be a string")
        
        # create attribute that is a dictionary of card point values
        self.cardpointvalues = {value:int(value) for value in Card.possiblecardvalues[:9]}
        self.cardpointvalues.update({value:10 for value in Card.possiblecardvalues[9:]})
        self.cardpointvalues.update({'A':11})
        
        # initialize variables
        self.showcards = False
        self.money = 1000 # starting amount
        self.dealer = dealer # dealer flag
        self.clear_hand() # creates and clears self.hand list

        # figure out names
        if name is None:
            name = "<unnamed>"
            if dealer:
                name = ""
        if dealer:
            name = "Dealer " + name
        self.name = name.strip()
                
    def set_showhand(self):
        self.showcards = True
        # make hand visible, used in __repr__ method

    def set_hidehand(self):
        self.showcards = False
        # make hand not visible, used in __repr__ method
    
    def get_handvalue(self):
        handvalue = sum([self.cardpointvalues[card.value] for card in self.hand])
        # get hand value (using 11 for all Aces)
        for card in self.hand:
            if handvalue > 21 and card.value == 'A':
                handvalue -=10
                # subract 10 for each Ace until under 21
        return handvalue
    
    def bet(self,betammount):
        if type(betammount) is not int:
            raise ValueError("betammount must be an int")
        if betammount > self.money:
            raise ValueError("cannot bet more than player has. Player has (), bet was ().".format(self.money,betammount))
        self.money -= betammount
        # remove money from Player when placing a bet
    
    def win(self,winnings):
        if type(winnings) is not int:
            raise ValueError("winnings must be an int")
        self.money += winnings
        # add winnings to player if win
        # winnings should include original bet + profit
    
    def get_moneyamount(self):
        return self.money
    
    def clear_hand(self):
        self.hand = []

    def take_card(self,card):
        if type(card) is not Card:
            raise ValueError("card must of of Card class")
        self.hand.append(card)
    
    def __repr__(self):
        # this method allows us to define what Player will look like
        # Also, we will be able to print(Player) once we define this
        # in this case, we can also control how the dealer shows/hides cards here
        
        if self.showcards:
            return self.name + ': ['+' '.join([card.__repr__() for card in self.hand])+']'
        elif self.dealer and len(self.hand)>1:
            return self.name + ': [** ' +' '.join([card.__repr__() for card in self.hand[1:]])+']'
        else:
            return self.name + ': ['+' '.join([' ** ' for card in self.hand])+']'




if __name__ == "__main__":
    # only run this code if running as stand-alone file
    # Initialization/Setup steps
    boot = Boot(6)
    name = input("Welcome to the BlackJack table! Please enter a name to play: ")
    if name == '':
        name = 'Bob'
        print("You didn't enter anything. We'll just call you 'Bob.'")
        print()
    player = Player(name)
    player.set_showhand()
    dealer = Player('Janet',dealer=True)
    Table = (player,dealer)
    print("dealer:")
    print(dealer)
    print("player:")
    print(player)
    print("Welcome, {}! you'll be playing against the dealer ({}).".format(name,dealer.name))

    # Gameplay begins
    while player.get_moneyamount()>0:
        playagain = input("Would you like to play the next hand?\n[Enter] to play, 'q' to quit: ")
        if (playagain+' ')[0].lower() == 'q':
            break
        elif playagain != '':
            print("I didn't understand your entry. Please try again...\n\n")
            continue
        print()
        bet = input("Please enter a bet amount (dollars as an int, [Enter] for default of 100)\nYou have ${}: ".format(player.get_moneyamount()))
        if bet == '':
            bet = 100
        elif not bet.isdigit():
            print("That's not a valid bet.\n\nPlease try again.")
            continue
        elif int(bet) > player.get_moneyamount():
            print("You do not have that much money. Please try again.")
            continue
        else:
            bet = int(bet)
        print("You bet ${}".format(bet))
        player.bet(bet)
        print("(You have ${} left.".format(player.get_moneyamount()))

        # Game Begins!
        print("...dealing cards...")
        for person in Table:
            person.clear_hand()
            # throw away any old cards
        dealer.set_hidehand()
        # hide dealer hand
        print("===== Dealing FIRST card... =====")
        for person in Table:
            person.take_card(boot.dealcard())
            print(person)
        print()
        print()
        
        print("===== Dealing SECOND card... =====")
        for person in Table:    
            person.take_card(boot.dealcard())
            print(person)

        # player actions start here
        print()
        print("===== Player's turn... =====")

        while True:
            print()
            print(dealer)
            print(player)
            print("you have {}. Would you like to hit?".format(player.get_handvalue()))
            play = input("[Enter] to stay, any other entry to hit: ")
            if play == '':
                break
            else:
                player.take_card(boot.dealcard())
        if player.get_handvalue() > 21:
            print("You busted with {}".format(player.get_handvalue()))
            print(player)
            print()
            print("You lost ${}".format(bet))
            print("Your current funds are: {}".format(player.get_moneyamount()))
        else:
            dealer.set_showhand()
            # show dealer hand when dealer starts to play

            # this is the dealer gameplay, hit until over 17 AND over player's value, unless player already busted
            while dealer.get_handvalue() < 21 and player.get_handvalue() <= 21 and (dealer.get_handvalue() <17 or player.get_handvalue() >= dealer.get_handvalue()):
                print ("Dealer has {}".format(dealer.get_handvalue()))
                print("Dealer hits")
                dealer.take_card(boot.dealcard())
                print(dealer)
                if dealer.get_handvalue() > 21:
                    print("Dealer busts, with {}!".format(dealer.get_handvalue()))
            

        if player.get_handvalue() > 21:
            pass
            #player already lost

        elif dealer.get_handvalue() > 21 or player.get_handvalue() >= dealer.get_handvalue():
            print(dealer)
            print("Player wins ${}!".format(bet))
            player.win(bet)
            player.win(bet)
            print("Player now has ${}".format(player.get_moneyamount()))
        else:
            print("Player loses.")
            print(player)
            print(player.get_handvalue())
            print(dealer)
            print(dealer.get_handvalue())
            print()
            print("You lost ${}".format(bet))
            print("Your current funds are: {}".format(player.get_moneyamount()))
    

