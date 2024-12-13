#!/bin/python3
import numpy as np
from typing import List

decks = {}

def size_of(deck):
	return round(sum(deck), 5)

def data_is_correct(decks: List) -> bool:
	"""
	The data is defined like this :
	all decks must be of the same size.
	Each index represents a card and the value is the probability of it to be in the deck.
	All values of probability additionned together is the amount of cards in the deck.
	For one card (index), all of the decks must have 1 if the probabilities of one card for all decks are additionned.
	"""
	decks_np = np.array(decks)
	sums = np.sum(decks_np, axis = 1) # y axis
	return np.count_nonzero(sums != 1) == 0 # only 1 in sums

def draw_card_unknown(deck_from, deck_to, draw=1):
	"""
	Changes the probabilities of the cards to belong to one deck if we don't know which card has been drawn.

	Keywords arguments:
	deck_from -- list : the probability of each card (represented by index) to be in the first deck 	
	deck_from -- list : the probability of each card (represented by index) to be in the target deck 	
	draw -- int : the number of cards that we want to draw.
	"""
	n_cards_from = size_of(deck_from)
	while draw > 0:
		if n_cards_from < 1:
			return
		for card, prob in enumerate(deck_from):
			prob_draw_card = (prob / n_cards_from)
			deck_from[card] -= prob_draw_card
			deck_to[card] += prob_draw_card
		n_cards_from = size_of(deck_from)
		draw -= 1

def draw_card_known(deck_from, deck_to, other_decks=0, *cards):
	"""
	Changes the probabilities of the cards to be in one deck if we know which card has been drawn.

	Keywords arguments:
	deck_from -- list : the probability of each card (represented by index) to be in the first deck 	
	deck_to -- list : the probability of each card (represented by index) to be in the target deck 	
	other_decks -- list : list of decks to which we will also apply probability absorption
	*cards -- *int : the cards that has been drawn

	"""
	for card in cards:
		if (size_of(deck_from) < 1.0):
			print(f"Not enough cards in deck {deck_from} to draw a card.")
			return
		proba_from = deck_from[card] # 0.6
		proba_to = deck_to[card] # 0.4
		deck_from[card] = 0.0
		deck_to[card] = 1.0
		to_del_from = 1 - proba_from # 0.4
		to_add_to = proba_to # 0.6
		size_from = size_of(deck_from)
		empty_to = sum([1 - c for c in deck_to])
		for i, card_proba in enumerate(deck_to):
			if i == card:
				continue
			deck_to[i] = round(card_proba + to_add_to * (1 - card_proba) / empty_to, 5)
			deck_from[i] = round(deck_from[i] - to_add_to * deck_from[i] / empty_to, 5)
		if isinstance(other_decks, list): # TODO TEST & DEBUG
			for deck in other_decks:
				deck[card] = 0.0
				proba_deck = deck[card]
				empty_deck = sum([1 - c for c in deck])
				for i, card_proba in enumerate(deck):
					deck[i] = round(card_proba + proba_deck * (1 - card_proba) / empty_deck, 5)
