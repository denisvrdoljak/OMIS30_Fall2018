#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:39:03 2018

@author: denisvrdoljak
"""


import random
import deckofcards
from ducksoccer import Duck
from ducksoccer import SoccerBall



myrandomint = random.choice(range(52))

mydeckofcards = deckofcards.Deck()
deck = mydeckofcards.deck.copy()
duck = Duck("Bob")
ball = SoccerBall()

while len(deck) > 1:
    #newrandomint = myrandomint % len(deck)
    newrandomint = random.choice(range(len(deck)))
    card = deck.pop(newrandomint)
    print("You picked a {} out of the deck.".format(card))
    
    if card.value in ['J','K','Q']:
        print("This is a face card. Skipping to next turn (e.g., continue statement in while loop)")
        continue
    
    card = deck.pop()
    print("You picked a {} out of the deck.".format(card))

    if card.suit == "Club":
        ball.kick()
    elif card.suit == 'Spade':
        duck.quack()
    else:
        print("Card wasn't a Club or a Spade. Moving to next turn (end of while loop iteration)")

    if (input("\nPress [Enter] to continue to next turn. Press 'q' to quit: ")+" ").lower()[0] == 'q':
        print("You chose to quit. Quitting...")
        break
else:
    print("The deck is empty.")
print("End of game. Thank you for playing.")